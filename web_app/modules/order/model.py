from sqlalchemy import Column, Integer, String
from marshmallow import Schema, fields, ValidationError, pre_load
from web_app.modules import db



class Order(db.Model):
    __tablename__ = 'order'
    id = Column(Integer, primary_key=True)
    title = Column(String)


class OrderSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str()
    # formatted_name = fields.Method("format_name", dump_only=True)

    # def format_name(self, order):
    #     return "{}, {}".format(order.id, order.title)

order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)