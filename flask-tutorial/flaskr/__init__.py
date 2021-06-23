import os

from flask import Flask



def create_app():
    app = ...
    # existing code omitted

    from . import db
    db.init_app(app)

    return app