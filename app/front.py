import os

from fastapi import FastAPI
from nicegui import ui

from app.chuck import chuck


def init(fastapi_app: FastAPI) -> None:
    ui.page("/", title="Chuck Norris Random Facts")(chuck)

    ui.run_with(
        fastapi_app,
        mount_path="/",  # NOTE this can be omitted if you want the paths passed to @ui.page to be at the root
        storage_secret=os.getenv("STORAGE", "__STORAGE__"),
    )