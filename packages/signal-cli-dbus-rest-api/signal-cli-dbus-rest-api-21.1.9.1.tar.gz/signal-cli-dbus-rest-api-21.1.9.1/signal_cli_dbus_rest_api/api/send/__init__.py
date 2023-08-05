"""
send messages to single contact or group
"""


from base64 import b64decode
from io import BytesIO
from mimetypes import guess_extension
from os import remove as os_remove
from tempfile import mkstemp
from uuid import uuid4

from magic import from_buffer
from sanic import Blueprint, Sanic
from sanic.log import logger
from sanic.response import json
from sanic_openapi import doc
from signal_cli_dbus_rest_api.lib.dbus import SignalCLIDBus
from signal_cli_dbus_rest_api.lib.helper import get_groupid_as_bytes, is_phone_number

send_v1 = Blueprint("send_v1", url_prefix="/send")
send_v2 = Blueprint("send_v2", url_prefix="/send")


def decode_attachments(attachments, uuid):
    """
    decode base64 attachments and dump the decoded
    content to disk for sending out later
    """
    decoded_attachments = []
    for index, attachment in enumerate(attachments):
        try:
            attachment_io_bytes = BytesIO()
            attachment_io_bytes.write(b64decode(attachment))
            extension = guess_extension(
                from_buffer(attachment_io_bytes.getvalue(), mime=True)
            )
            _, filename = mkstemp(
                prefix=f"{uuid}_{index}_", suffix=f".{extension}")
            with open(filename, "wb") as f_h:
                f_h.write(b64decode(attachment))
            decoded_attachments.append(filename)
        # pylint: disable=broad-except
        except Exception as err:
            logger.error("unable to decode attachment: %s", err)
    return decoded_attachments


def send_message(
    recipients: list, number: str, message: str, attachments: list, version: int = 2
):
    """
    send message
    """
    try:
        dbus = SignalCLIDBus(number=number)
        real_recipients = is_phone_number(
            recipients=recipients, dbus_connection=dbus.dbusconn
        )
        method = dbus.dbusconn.sendMessage
        signature = "sasas"
        if not real_recipients:
            real_recipients = get_groupid_as_bytes(
                recipient=recipients[0], version=version
            )
            method = dbus.dbusconn.sendGroupMessage
            signature = "sasay"
        if not real_recipients:
            return (
                {
                    "error": f"{recipients} is neither a phone number nor a valid group id",
                },
                400,
            )
        timestamp = method(message, attachments, real_recipients, signature=signature)
        return {"timestamp": str(timestamp)}, 201
    # pylint: disable=broad-except
    except Exception as err:
        logger.error(err)
        return {"error": err.__repr__()}, 400
    finally:
        for attachment in attachments:
            os_remove(attachment)


@send_v2.post("/", version=2)
@doc.tag("Messages")
@doc.consumes(
    doc.JsonBody(
        {
            "base64_attachments": doc.List(doc.String()),
            "message": doc.String(),
            "number": doc.String(),
            "recipients": doc.List(doc.String()),
        },
    ),
    required=True,
    location="body",
)
@doc.response(201, {"timestamp": str}, description="Created")
@doc.response(400, {"error": str}, description="Bad Request")
@doc.description("Send a signal message.")
async def send_v2_post(request):
    """
    Send a signal message.
    """
    if not request.json:
        return json({"error": "missing json payload"}, 400)
    decoded_attachments = []
    app = Sanic.get_app()
    recipients = request.json.get("recipients")
    try:
        number = request.json.get("number") or app.config.ACCOUNT
    except AttributeError:
        return json(
            {"error": "number missing in request and SIGNAL_CLI_DBUS_REST_API_ACCOUNT unset "},
            400
        )
    message = request.json.get("message")
    attachments = request.json.get("base64_attachments")
    uuid = str(uuid4())
    if isinstance(attachments, list):
        decoded_attachments = decode_attachments(attachments, uuid)
    return_message, return_code = send_message(
        recipients, number, message, decoded_attachments
    )
    return json(return_message, return_code)


@send_v1.post("/<recipient:path>", version=1)
@doc.tag("Messages")
@doc.consumes(
    doc.JsonBody(
        {
            "base64_attachments": doc.List(doc.String()),
            "message": doc.String(),
            "number": doc.String(),
        },
    ),
    required=True,
    location="body",
)
@doc.consumes(doc.String(name="recipient"), location="path")
@doc.response(201, {"timestamp": str}, description="Created")
@doc.response(400, {"error": str}, description="Bad Request")
@doc.description("Send a signal message.")
async def send_v1_post(request, recipient):
    """
    Send a signal message.
    """
    if not request.json:
        return json({"error": "missing json payload"}, 400)
    decoded_attachments = []
    app = Sanic.get_app()
    try:
        number = request.json.get("number") or app.config.ACCOUNT
    except AttributeError:
        return json(
            {"error": "number missing in request and SIGNAL_CLI_DBUS_REST_API_ACCOUNT unset "},
            400
        )
    message = request.json.get("message")
    attachments = request.json.get("base64_attachments")
    uuid = str(uuid4())
    if isinstance(attachments, list):
        decoded_attachments = decode_attachments(attachments, uuid)
    return_message, return_code = send_message(
        [recipient], number, message, decoded_attachments, version=1
    )
    return json(return_message, return_code)
