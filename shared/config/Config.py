import json
from pathlib import Path

from pydantic import BaseModel
from pydantic.tools import parse_obj_as


class TelegramConfig(BaseModel):
    bot_token: str
    allowed_users: list


class APINinjasConfig(BaseModel):
    api_ninjas_token: str
    api_ninjas_categories: list


class GoogleTranslateConfig(BaseModel):
    message: str
    language: str


class Config(BaseModel):
    telegram: TelegramConfig
    api_ninjas: APINinjasConfig
    google_translate: GoogleTranslateConfig


class ConfigHandler:
    def __init__(
            self,
            config_path: Path
    ) -> None:
        self.config_path = config_path

        if not self.config_path:
            raise Exception(
                f"Config file at {self.config_path.absolute()} doesn't exist"
            )


    def load(self) -> Config:
        with open(self.config_path, mode='r') as handle:
            contents = handle.read()
            config = parse_obj_as(Config, json.loads(contents))

            return config
