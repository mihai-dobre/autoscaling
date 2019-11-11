import os
from src import logger
from src.api import create_app, db
logger.setLevel("INFO")
env = os.getenv("FLASK_ENV") or "dev"
print(f"Active environment: * {env} *")
app = create_app(env)

