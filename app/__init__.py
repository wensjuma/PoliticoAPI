import os 
from flask import Flask
from app.api.v1.views import party_view
from app.api.v1.views import offices
from config import app_config

def create_app(app_config):
    app= Flask(__name__)
    app.config.from_object([app_config])
    app.register_blueprint(party_view.party_route)
    app.register_blueprint(offices.office_route)

    return app
