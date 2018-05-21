from flask import Blueprint, jsonify, json
from flask_restful import Api, Resource

from order.modules.order.model import Order,orders_schema,order_schema

order = Blueprint(
    'order', #name of module
    __name__,
    template_folder='templates' # templates folder
)
api = Api(order)


class OrderApi(Resource):
    def get(self):
        data = Order.query.all()
        result = orders_schema.dump(data)
        return jsonify({'order': result.data})


class OrderGet(Resource):
    def get(self, id):
        data = Order.query.filter_by(id=id)
        result = orders_schema.dump(data)
        return jsonify({'order': result.data})


api.add_resource(OrderApi,'/')
api.add_resource(OrderGet,'/<int:id>')
