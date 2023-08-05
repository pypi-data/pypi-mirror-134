"""
send message reactions to single contact
"""


from sanic import Blueprint
from sanic.log import logger
from sanic.response import json
from sanic_openapi import doc
from signal_cli_dbus_rest_api.lib.dbus import SignalCLIDBus
from signal_cli_dbus_rest_api.lib.helper import get_groupid_as_bytes, is_phone_number

reactions_v1 = Blueprint("reactions_v1", url_prefix="/reactions")


def send_reaction(
    number: str,
    reaction: str,
    remove: bool,
    recipients: str,
    target_author: str,
    timestamp: int,
):  # pylint: disable=too-many-arguments
    """
    send reaction
    """
    try:
        if not isinstance(recipients, list):
            recipients = [recipients]
        dbus = SignalCLIDBus(number=number)
        real_recipients = is_phone_number(
            recipients=recipients, dbus_connection=dbus.dbusconn
        )
        method = dbus.dbusconn.sendMessageReaction
        signature = "sbsxas"
        if not real_recipients:
            real_recipients = get_groupid_as_bytes(recipient=recipients[0])
            method = dbus.dbusconn.sendGroupMessageReaction
            signature = "sbsxay"
        if not real_recipients:
            return (
                {
                    "error": f"{recipients} is neither a phone number nor a valid group id"
                },
                400,
            )
        result = method(
            reaction,
            remove,
            target_author,
            timestamp,
            real_recipients,
            signature=signature,
        )
        return {"timestamp": str(result)}, 201
    # pylint: disable=broad-except
    except Exception as err:
        logger.error(err)
        return {"error": err.__repr__()}, 400


reactions_v1_params_post = doc.JsonBody(
    {
        "reaction": doc.String(
            description="Unicode grapheme cluster of the emoji", required=True
        ),
        "remove": doc.Boolean(
            description="Whether a previously sent reaction (emoji) should be removed"
        ),
        "recipient": doc.String(
            description="String with the phone number of a single recipient."
        ),
        "recipients": doc.List(
            doc.String(
                description="String with the phone number of a single recipient"
            ),
            description="List of strings with the phone numbers of a multiple recipient",
        ),
        "target_author": doc.String(
            description=(
                "String with the phone number of the author "
                "of the message to which to react"
            ),
            required=True,
        ),
        "timestamp": doc.Integer(
            description="Will be used to identify the corresponding Signal reply",
            required=True,
        ),
    }
)


@reactions_v1.post("/<number:path>", version=1)
@doc.tag("Reactions")
@doc.consumes(reactions_v1_params_post, required=True, location="body")
@doc.consumes(doc.String(name="number"), location="path")
@doc.response(201, {"timestamp": str}, description="Created")
@doc.response(400, {"error": str}, description="Bad Request")
@doc.description(
    "Send a reaction. Request must include either `recipient` or `recipients`!"
)
async def reactions_v1_post(request, number):
    """
    Send a reaction.
    """
    if not request.json:
        return json({"error": "missing json payload"}, 400)
    for key, value in reactions_v1_params_post.fields.items():
        if value.required and not request.json.get(key):
            return json({"error": f"missing parameter: {key}"}, 400)
    if not request.json.get("recipient") or request.json.get("recipients"):
        return json(
            {
                "error": "missing either parameter recipient (str) or recipients (list of strings)"
            },
            400,
        )
    return_message, return_code = send_reaction(
        number=number,
        reaction=request.json.get("reaction"),
        remove=request.json.get("remove"),
        target_author=request.json.get("target_author"),
        timestamp=request.json.get("timestamp"),
        recipients=request.json.get("recipients", request.json.get("recipient")),
    )
    return json(return_message, return_code)
