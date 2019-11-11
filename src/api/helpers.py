from time import sleep
from celery import Celery

from src import logger
from src.config import BaseConfig as Config

redis_url = Config.BROKER_URL
app = Celery("tasks", broker=redis_url, backend=redis_url)


@app.task
def add(data):
    fat_data = [1]*15000
    sleep(60 * 5)
    logger.info("Adding {} and {}".format(data['a'], data['b']))
    return data['a'] + data['b']
