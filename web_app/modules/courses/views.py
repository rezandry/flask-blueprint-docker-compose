from flask import Blueprint
from flask_restful import Api, Resource


course = Blueprint(
    'course', __name__
)
api = Api(course)


class GetCourse(Resource):
    def get(self):
        from web_app.modules.courses.model import Courses
        data = Courses.query.all()
        value = []
        for d in data:
            d_dict = d.to_dict()
            value.append(d_dict)
        return value

api.add_resource(GetCourse, '/api/course')
