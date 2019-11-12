from flask import Flask, jsonify


def create_app(env=None):
    """Create a Flask application using the app factory pattern."""

    # instantiate the app
    app = Flask(__name__)

    # set config
    from src.config import config_by_name

    app.config.from_object(config_by_name[env or "test"])

    # register blueprints
    from src.api.routes import bp as api_bp

    app.register_blueprint(api_bp)

    # health check end point
    @app.route("/health")
    def health_check():
        """
        Returns 200 OK if health checks pass
        """
        return jsonify({"status": "API OK."})

    return app
