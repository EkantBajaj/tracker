from flask_restful import Resource
import requests
from .config import tracking_api_url

class hello(Resource):
    def get(self):
        return 'hello world'

class OrderDetailsResource(Resource):
    def get(self,awb_no):
        params = {'awb':awb_no}
        response = requests.get(tracking_api_url,params=params)
        return response.json()