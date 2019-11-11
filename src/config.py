import os


class BaseConfig:
    NAME = "base"
    REQUEST_TIME_OUT = 15
    BROKER_URL = os.environ.get("BROKER_URL")
    PING_DELAY = 5
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    NAME = "dev"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class TestingConfig(BaseConfig):
    NAME = "test"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_TEST_URL")
    BROKER_URL = "redis://"


class ProductionConfig(BaseConfig):
    NAME = "prod"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


EXPORT_CONFIGS = [DevelopmentConfig, TestingConfig, ProductionConfig]
config_by_name = {cfg.NAME: cfg for cfg in EXPORT_CONFIGS}
