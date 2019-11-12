import os


class BaseConfig:
    NAME = "base"
    REQUEST_TIME_OUT = 15
    BROKER_URL = os.environ.get("BROKER_URL")
    PING_DELAY = 5


class DevelopmentConfig(BaseConfig):
    NAME = "dev"


class TestingConfig(BaseConfig):
    NAME = "test"
    BROKER_URL = "redis://"


class ProductionConfig(BaseConfig):
    NAME = "prod"


EXPORT_CONFIGS = [DevelopmentConfig, TestingConfig, ProductionConfig]
config_by_name = {cfg.NAME: cfg for cfg in EXPORT_CONFIGS}
