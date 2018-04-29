from flask_restful import fields
from marshmallow import Schema

from web_app.modules import db
from sqlalchemy import Integer, Column, String


class Courses(db.Model):
    __tablename__ = 'course'
    id = db.Column(Integer, primary_key= True)
    title = db.Column(String)
    url = db.Column(String)
    description = db.Column(String)

    def to_dict(self):
        data = {}
        data['id'] = self.id
        data['title'] = self.title
        data['url'] = self.url
        data['description'] = self.description
        return data


class CourseSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str()
    url = fields.Str()
    description = fields.Str()


course_schema = CourseSchema()
course_schema = CourseSchema(many=True)