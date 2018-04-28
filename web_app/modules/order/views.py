from flask import Blueprint, jsonify, json
from flask_restful import Api, Resource

from web_app.modules.order.model import Order
from flask.ext.jsontools import jsonapi

mod_order = Blueprint(
    'mod_order', #name of module
    __name__,
    template_folder='templates' # templates folder
)
api = Api(mod_order)

class TodoItem(Resource):
    @jsonapi
    def get(self):
        # query dari database
        data = Order.query.all()

        # data = [s
        #         {"id": 1, "title":"Flask vs Golang"},
        #         {"id": 2, "title":"Best Python framework out there?"},
        #         {"id": 3, "title":"What to do using python in machine learning"}
        #     ]
        return data


api.add_resource(TodoItem, '/order')
