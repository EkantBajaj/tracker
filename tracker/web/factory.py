from flask import Flask
from tracker.web.restful import create_restful_api

def create_app():

    app = Flask(__name__)
    rest_api = create_restful_api(application_root='/api')
    app.register_blueprint(rest_api,url_prefix='/api')
    return app