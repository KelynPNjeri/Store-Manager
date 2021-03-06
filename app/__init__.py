from flask import Flask, Blueprint
from instance.config import app_config
from flask_jwt_extended import JWTManager



def create_app(config_name="development"):

    app = Flask(__name__)
    
    
    app.config['JWT_SECRET_KEY'] = 'Veritasistruth'

    from .api.v1 import version1 as v1
    app.register_blueprint(v1)

    auth = JWTManager(app)


    return app
