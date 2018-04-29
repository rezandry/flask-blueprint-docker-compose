from flask import Blueprint, jsonify, json
from flask_restful import Api, Resource

from web_app.modules.order.model import Order,order_schema,orders_schema

mod_order = Blueprint(
    'order', #name of module
    __name__,
    template_folder='templates' # templates folder
)
api = Api(mod_order)

class OrderApi(Resource):
    def get(self):
        data = Order.query.all()
        result = orders_schema.dump(data)
        return jsonify({'orders': result.data})

api.add_resource(OrderApi,'/order/')
