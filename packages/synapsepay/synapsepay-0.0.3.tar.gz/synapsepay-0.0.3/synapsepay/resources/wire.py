from ..apibits import *
from .. import Client
from . import *

class Wire(APIResource):

    # Everything below here is used behind the scenes.
    def __init__(self, *args, **kwargs):
    	super(Wire, self).__init__(*args, **kwargs)
    	APIResource.register_api_subclass(self, "wire")

    _api_attributes = {
        "date" : {},
        "fee" : {},
        "memo" : {},
        "routing_number_string" : {},
        "status" : {},
        "status_url" : {},
        "amount" : {},
        "id" : {},
        "reference_id" : {},
        "resource_uri" : {},
        "account_number_string" : {},
    }
