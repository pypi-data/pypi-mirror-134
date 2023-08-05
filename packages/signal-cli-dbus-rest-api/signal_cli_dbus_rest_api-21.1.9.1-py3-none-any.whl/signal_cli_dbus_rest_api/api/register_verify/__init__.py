"""
register and verify
"""

from sanic import Blueprint
from sanic.log import logger
from sanic.response import json
from sanic_openapi import doc
from signal_cli_dbus_rest_api.lib.dbus import SignalCLIDBus

register = Blueprint("register", url_prefix="/register")
verify = Blueprint("verify", url_prefix="/register")


@register.post("/<number:path>", version=1)
@doc.tag("Devices")
@doc.consumes(
    doc.String(name="number", description="Registered Phone Number"),
    location="path",
    required=True,
)
@doc.consumes(
    doc.JsonBody(
        {
            "captcha": doc.String(),
            "use_voice": doc.Boolean(),
        }
    ),
    location="body",
)
@doc.response(201, None, description="OK")
@doc.response(400, {"error": str}, description="Bad Request")
@doc.description("Register a phone number with the signal network.")
async def register_post(request, number):
    """
    Register a phone number.
    """
    if not request.json:
        return json({"success": "false", "message": "missing json payload"}, 500)
    use_voice = request.json.get("use_voice", False)
    captcha = request.json.get("captcha")
    opts = [number, use_voice]
    try:
        dbus = SignalCLIDBus()
        if captcha:
            method = dbus.pydbusconn.registerWithCaptcha
            opts.append(captcha)
        else:
            method = dbus.pydbusconn.register
        result = method(*opts)
        # successful verification just returns None
        if result:
            logger.info(result)
            return json({"error": result}, 400)
        return json(None, 200)
    # pylint: disable=broad-except
    except Exception as err:
        logger.error(err)
        return json({"error": err.__repr__()}, 400)


@verify.post("/<number:path>/verify/<token:path>", version=1)
@doc.tag("Devices")
@doc.consumes(
    doc.String(name="number", description="Registered Phone Number"),
    location="path",
)
@doc.consumes(
    doc.String(name="token", description="Verification Code"),
    location="path",
)
@doc.consumes(
    doc.JsonBody(
        {
            "pin": doc.String(),
        }
    ),
    location="body",
)
@doc.response(201, None, description="OK")
@doc.response(400, {"error": str}, description="Bad Request")
@doc.description("Verify a registered phone number with the signal network.")
async def verify_post(request, number, token):
    """
    Verify a registered phone number.
    """
    pin = None
    if request.json:
        pin = request.json.get("pin")
    opts = [number, token]
    try:
        dbus = SignalCLIDBus()
        if pin:
            method = dbus.pydbusconn.verifyWithPin
            opts.append(pin)
        else:
            method = dbus.pydbusconn.verify
        result = method(*opts)
        # successful verification just returns None
        if result:
            logger.info(result)
            return json({"error": result}, 400)
        return json(None, 200)
    # pylint: disable=broad-except
    except Exception as err:
        logger.error(err)
        return json({"error": err.__repr__()}, 400)
