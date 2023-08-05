"""
about
"""

from sanic import Blueprint
from sanic.response import json
from sanic_openapi import doc

about_v1 = Blueprint("about_v1", url_prefix="/about")


@about_v1.get("/", version=1)
@doc.tag("General")
@doc.produces(
    {
        "mode": doc.String(),
        "versions": doc.List(doc.String()),
    },
    description="OK",
    content_type="application/json",
)
@doc.description("Returns the supported API versions.")
async def about_v1_get(request):  # pylint: disable=unused-argument
    """
    Lists general information about the API.
    """
    return json(
        {
            "mode": "dbus",
            "versions": ["v1", "v2"],
        },
        200
    )
