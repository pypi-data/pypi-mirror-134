import os

from pydantic import BaseSettings


class ProductionConfig(BaseSettings):
    app_name: str = "Gigalogy Platform Monitor API"
    app_description: str = "Monitors all the containers running in Gigalogy platform and send slack notification when something goes wrong"
    app_version: str = "v1"
    app_logo_url: str = "https://www.gigalogy.com/img/favicon.png"
    env_name: str = "PROD"
    allowed_hosts: str = os.environ["ALLOWED_HOSTS"]
    slack_webhook_url: str = os.environ["SLACK_WEBHOOK_URL"]


class StagingConfig(BaseSettings):
    app_name: str = "Gigalogy Platform Monitor API"
    app_description: str = "Monitors all the containers running in Gigalogy platform and send slack notification when something goes wrong"
    app_version: str = "v1"
    app_logo_url: str = "https://www.gigalogy.com/img/favicon.png"
    env_name: str = "STG"
    allowed_hosts: str = os.environ["ALLOWED_HOSTS"]
    slack_webhook_url: str = os.environ["SLACK_WEBHOOK_URL"]


if os.environ["APP_ENVIRONMENT"] == "PROD":
    config = ProductionConfig()
elif os.environ["APP_ENVIRONMENT"] == "STG":
    config = StagingConfig()