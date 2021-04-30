from flask import Flask, request, jsonify
from flask_restplus import Api, Resource, fields

from course.course_service import CourseService
from db import db
from ma import ma

app = Flask(__name__)
app.config.from_pyfile('config.py')


@app.before_first_request
def create_tables():
    db.create_all()


# TODO: add blueprints
# TODO: add unittests

api = Api(app)
db.init_app(app)
ma.init_app(app)

ns = api.namespace('courses', description='Courses operations')

course_expected_model = api.model('Course', {
    'id': fields.Integer(readonly=True),
    'name': fields.String(),
    'start_date': fields.Date(),
    'end_date': fields.Date(),
    'number_of_lectures': fields.Integer
})


@ns.route('/')
class CourseListResource(Resource):
    @ns.doc('Get list of courses')
    def get(self):
        return CourseService.get_all()

    @ns.doc('Add new course')
    @ns.expect(course_expected_model)
    def post(self):
        return CourseService.create(request)


# TODO: add the last request
# @ns.route('/<name>')
# class D(Resource):
#     def get(self, name, start_date, end_date):
#         courses_list = db.session.query(CourseModel).filter(CourseModel.name == name).all()
#         courses_list = db.session.query(CourseModel).filter(CourseModel.start_date=start_date)
#         return jsonify(serialize_list(courses_list))


@ns.route('/<int:id>')
class CourseResource(Resource):
    @ns.doc('Get course by id', params={'id': 'Id'})
    def get(self, id):
        return CourseService.get_by_id(id)

    @ns.doc('Change course', params={'id': 'Id'})
    @ns.expect()
    def put(self, id):
        pass

    @ns.doc('Delete course by id', params={'id': 'Id'})
    def delete(self, id):
        CourseService.delete_by_id(id)
        return jsonify(dict(status='Success', id=id))


# # TODO: add error handling
# @ns.errorhandler(marshmallow.exceptions.ValidationError)
# def course_not_found(error):
#     return jsonify({'message': 'Not found', 'code': '444'})


if __name__ == '__main__':
    app.run()
