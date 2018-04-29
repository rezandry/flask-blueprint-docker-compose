from sqlalchemy import Column, Integer, String
from marshmallow import Schema, fields, ValidationError, pre_load
from web_app.modules import db


class Course(db.Model):
    __tablename__ = 'course'
    id = db.Column(Integer, primary_key=True)
    title = db.Column(String)


class CourseSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str()


course_schema = CourseSchema()
courses_schema = CourseSchema(many=True)