from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# instantiate the extensions
db = SQLAlchemy()
migrate = Migrate()


def create_app(env=None):
    """Create a Flask application using the app factory pattern."""

    # instantiate the app
    app = Flask(__name__)

    # set config
    from src.config import config_by_name

    app.config.from_object(config_by_name[env or "test"])

    # set up extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # register blueprints
    from src.api.routes import bp as api_bp

    app.register_blueprint(api_bp)

    # shell context for flask cli
    @app.shell_context_processor
    def make_shell_context():
        from src.models import PDSJob

        return {"db": db, "PDSJob": PDSJob}

    # health check end point
    @app.route("/health")
    def health_check():
        """
        Returns 200 OK if health checks pass
        """
        return jsonify({"status": "API OK."})

    return app
