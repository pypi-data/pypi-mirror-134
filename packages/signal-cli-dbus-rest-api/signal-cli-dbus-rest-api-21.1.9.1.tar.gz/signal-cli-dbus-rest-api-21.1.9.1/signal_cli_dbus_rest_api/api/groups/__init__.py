"""
groups handler
"""

from sanic import Blueprint
from sanic.log import logger
from sanic.response import json
from sanic_openapi import doc
from signal_cli_dbus_rest_api.lib.dbus import SignalCLIDBus
from signal_cli_dbus_rest_api.lib.helper import get_group_properties

groups_for_number = Blueprint("groups_of_number", url_prefix="/groups")
group_details = Blueprint("group_details", url_prefix="/groups")


@groups_for_number.get("/<number>", version=1)
@doc.tag("Groups")
@doc.consumes(doc.String(name="number", description="Registered Phone Number"), location="path")
@doc.produces(
    [
        {
            "blocked": doc.Boolean(),
            "id": doc.String(),
            "internal_id": doc.String(),
            "invite_link": doc.String(),
            "members": doc.List(doc.String()),
            "name": doc.String(),
            "pending_invites": doc.List(doc.String()),
            "pending_requests": doc.List(doc.String()),
            "message_expiration_timer": doc.Integer(),
            "admins": doc.List(doc.String()),
            "description": doc.String(),
        }
    ],
    description="OK",
    content_type="application/json",
)
@doc.response(400, {"error": str}, description="Bad Request")
@doc.description("List all Signal Groups.")
async def groups_for_number_get(request, number):  # pylint: disable=unused-argument
    """
    List all Signal Groups.
    """
    try:
        dbus = SignalCLIDBus(number=number)
        groups = dbus.pydbusconn.listGroups()
        result = []
        for group in groups:
            success, data = get_group_properties(
                systembus=dbus.pydbus,
                objectpath=group[0],
            )
            if not success:
                return json({"error": result}, 400)
            result.append(data)
        return json(result, 200)
    # pylint: disable=broad-except
    except Exception as err:
        logger.error(err)
        return json({"error": err.__repr__()}, 400)


@group_details.get("/<number>/<groupid:path>", version=1)
@doc.tag("Groups")
@doc.consumes(doc.String(name="number", description="Registered Phone Number"), location="path")
@doc.consumes(
    doc.String(
        name="groupid",
        description="Group ID (hint: you'll need to replace forwards slash / with underscore _)"
    ),
    location="path"
)
@doc.produces(
    {
        "blocked": doc.Boolean(),
        "id": doc.String(),
        "internal_id": doc.String(),
        "invite_link": doc.String(),
        "members": doc.List(doc.String()),
        "name": doc.String(),
        "pending_invites": doc.List(doc.String()),
        "pending_requests": doc.List(doc.String()),
        "message_expiration_timer": doc.Integer(),
        "admins": doc.List(doc.String()),
        "description": doc.String(),
    },
    description="OK",
    content_type="application/json",
)
@doc.response(400, {"error": str}, description="Bad Request")
@doc.description("List a Signal Group.")
async def groups_of_number_get(
    request, number, groupid
):  # pylint: disable=unused-argument
    """
    List a Signal Group.
    """
    try:
        dbus = SignalCLIDBus()
        success, data = get_group_properties(
            systembus=dbus.pydbus,
            number=number,
            groupid=groupid,
        )
        if not success:
            return json({"error": data}, 400)
        return json(data, 200)
    # pylint: disable=broad-except
    except Exception as err:
        logger.error(err)
        return json({"error": err.__repr__()}, 400)
