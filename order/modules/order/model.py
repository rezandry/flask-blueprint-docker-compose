from sqlalchemy import Column, Integer, String
from marshmallow import Schema, fields, ValidationError, pre_load
from order.modules import db


class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(Integer, primary_key=True)
    title = db.Column(String)


class OrderSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str()


order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)