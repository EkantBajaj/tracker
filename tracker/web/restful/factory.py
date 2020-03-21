from flask_restful import Api
from tracker.web.subapp import SubApp
from tracker.web.restful.shipment import hello,OrderDetailsResource

def create_restful_api(application_root=None):
    blueprint = SubApp('restful', __name__)
    api = Api(blueprint)

    api.add_resource(hello,'/hello/')
    api.add_resource(OrderDetailsResource,'/track/<string:awb_no>')

    return blueprint