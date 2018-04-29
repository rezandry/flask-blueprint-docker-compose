from flask import Blueprint, jsonify, json
from flask_restful import Api, Resource

from web_app.modules.course.model import Course,course_schema,courses_schema

course = Blueprint(
    'course', #name of module
    __name__,
    template_folder='templates' # templates folder
)
api = Api(course)

class CourseApi(Resource):
    def get(self):
        data = Course.query.all()
        result = courses_schema.dump(data)
        return jsonify({'courses': result.data})

api.add_resource(CourseApi,'/course/')
