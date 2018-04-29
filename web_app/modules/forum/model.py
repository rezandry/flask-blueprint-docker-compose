from sqlalchemy import Column, Integer, String
from marshmallow import Schema, fields, ValidationError, pre_load
from web_app.modules import db

class Forum(db.Model):
    __tablename__ = 'forum'
    id = Column(Integer, primary_key=True)
    title = Column(String)


class ForumSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str()


forum_schema = ForumSchema()
forums_schema = ForumSchema(many=True)