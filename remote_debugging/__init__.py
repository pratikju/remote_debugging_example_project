from remote_debugging.store import configure_db_with_app
from remote_debugging.utils.config import Config
from remote_debugging.utils.flask import APIFlask


def create_app() -> APIFlask:

    app = APIFlask(__name__, instance_relative_config=True)
    app.config.from_object(Config)

    # NOTE: Order matters here
    configure_db_with_app(app)
    _register_all_blueprints(app)

    return app


def _register_all_blueprints(app: APIFlask):
    from remote_debugging.api import health, sample

    app.register_blueprint(health.blueprint)
    app.register_blueprint(sample.blueprint)
