import time
import uuid
from pathlib import Path

from flask import Blueprint, abort, jsonify, request, url_for

from src import logger
from src.api.helpers import add

bp = Blueprint("api", __name__)


@bp.route("/ping")
def ping():
    return jsonify({"status": "success", "message": "pong"})


@bp.route("/add", methods=["POST"])
def add_job():
    """
    Runs sum.
    Expected format of response:
    {
        "sum": "<sum of a and b>"
    }
    """
    logger.info("Serving add endpoint.")
    data = request.json
    logger.info(f"Calling celery worker with arguments {data}.")
    add.delay(data)
    return jsonify({'status': 'created'}), 201
