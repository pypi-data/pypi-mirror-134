"""
search handler
"""

from sanic import Blueprint
from sanic.log import logger
from sanic.response import json
from sanic_openapi import doc
from signal_cli_dbus_rest_api.lib.dbus import SignalCLIDBus

search_v1 = Blueprint("search_v1", url_prefix="/search")


@search_v1.get("/", version=1)
@doc.tag("Search")
@doc.consumes(
    doc.List(
        doc.String(),
        name="numbers",
        description="Numbers to check"
    ),
    required=True,
    location="query"
)
@doc.response(
    200,
    [
        {
            "number": doc.String(),
            "registered": doc.Boolean(),
        },
    ],
    description="OK"
)
@doc.response(400, {"error": str}, description="Bad Request")
@doc.description("Check if one or more phone numbers are registered with the Signal Service.")
async def search_v1_get(request):
    """
    Check if one or more phone numbers are registered with the Signal Service.
    """
    if not request.args:
        return json({"error": "missing query"}, 400)
    numbers = request.args.getlist("numbers")
    if not isinstance(numbers, list):
        return json({"error": "expecting numbers as list of strings"}, 400)
    try:
        dbus = SignalCLIDBus()
        accounts = dbus.pydbusconn.listAccounts()
        network_result = []
        result = []
        for account in accounts:
            account_dbus = SignalCLIDBus(account=account)
            network_result = account_dbus.dbusconn.isRegistered(
                numbers,
                signature="as",
            )
            if network_result:
                break
        data = dict(zip(numbers, network_result))
        for key, value in data.items():
            result.append(
                {
                    "number": key,
                    "registered": bool(value),
                }
            )
        return json(result, 200)
    # pylint: disable=broad-except
    except Exception as err:
        logger.error(err)
        return json({"error": err.__repr__()}, 400)
