from flask import Blueprint, request

from remote_debugging.store.repos import SampleRepo
from remote_debugging.utils.flask import APISuccess, APIResponse

blueprint = Blueprint("sample", __name__, url_prefix="/api/v1")


@blueprint.route("/test", methods=["POST"])
def test() -> APIResponse:
    data = request.json or request.form.to_dict()
    SampleRepo().create(data=data)
    return APISuccess(data)
