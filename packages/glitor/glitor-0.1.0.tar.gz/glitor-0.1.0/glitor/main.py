import docker
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.trustedhost import TrustedHostMiddleware

from glitor.config import config

client = docker.from_env()


def get_app():
    app = FastAPI(
        title=config.app_name,
        description=config.app_description,
        version=config.app_version,
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.add_middleware(TrustedHostMiddleware, allowed_hosts=config.allowed_hosts)

    return app


