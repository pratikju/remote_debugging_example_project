from flask import Blueprint

from remote_debugging.utils.flask import APISuccess

blueprint = Blueprint("health", __name__)


@blueprint.route("/health")
def health() -> APISuccess:
    return APISuccess("healthy")
