import os
from functools import lru_cache
from kombu import Queue
import sqlite3

def route_task(name, args, kwargs, options, task=None, **kw):
    return {"queue": "fibonacci"}


class BaseConfig:
    CELERY_BROKER_TRANSPORT: str  = "sqlalchemy"
    CELERY_BROKER_URL: str = os.environ.get("CELERY_BROKER_URL", "sqla+sqlite:///queue.sqlite")
    CELERY_RESULT_BACKEND: str = os.environ.get("CELERY_RESULT_BACKEND", "db+sqlite:///resultdb.sqlite")

    CELERY_TASK_QUEUES: list = (
        # default queue
        Queue("celery"),
        # custom queue
        Queue("fibonacci"),
    )

    CELERY_TASK_ROUTES = (route_task,)


class DevelopmentConfig(BaseConfig):
    pass


@lru_cache()
def get_settings():
    config_cls_dict = {
        "development": DevelopmentConfig,
    }
    config_name = os.environ.get("CELERY_CONFIG", "development")
    config_cls = config_cls_dict[config_name]
    return config_cls()


settings = get_settings()
