import os 
from flask import Flask
from config import app_config
from app.api.v2.models.database import init_db

def create_app(app_config):
    app= Flask(__name__)
    app.config.from_object([app_config])
    init_db

    from app.api.v1.views import party_view
    app.register_blueprint(party_view.party_route)

    from app.api.v1.views import offices
    app.register_blueprint(offices.office_route)

    from app.api.v2.views.parties import party_blueprints
    app.register_blueprint(party_blueprints)

    from app.api.v2.views.users import user_blueprints
    app.register_blueprint(user_blueprints)
    
    
    return app
