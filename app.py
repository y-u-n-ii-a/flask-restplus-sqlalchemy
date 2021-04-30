from datetime import datetime

from flask import Flask, request, jsonify, abort
from flask_restplus import Api, Resource, fields

from course_model1 import serialize_list, deserialize
from db import db
from course_service import CourseService

app = Flask(__name__)
app.config.from_pyfile('config.py')


@app.before_first_request
def create_tables():
    db.create_all()

# TODO: add marshmallow
# TODO: add blueprints

api = Api(app)
db.init_app(app)

ns = api.namespace('courses', description='Courses operations')

course_model = api.model('Course', {
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
        return jsonify(serialize_list(CourseService.get_all()))

    @ns.doc('Add new course')
    @ns.expect(course_model)
    def post(self):
        print(request.data)
        return jsonify(CourseService.create(request).serialize())


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
        return jsonify(CourseService.get_by_id(id))

    # @ns.doc('Change course', params={'id': 'Id'})
    # @ns.expect(course_model)
    # def put(self, id):
    #     course = db.session.query(CourseModel).filter(CourseModel.id == id).first_or_404()
    #
    #     # TODO: provide for the addition of not all fields
    #     course.name = request.json['name']
    #     course.start_date = datetime.strptime(request.json['start_date'], '%d/%m/%y')
    #     course.end_date = datetime.strptime(request.json['end_date'], '%d/%m/%y')
    #     course.number_of_lectures = request.json['number_of_lectures']
    #
    #     db.session.commit()

    @ns.doc('Delete course by id', params={'id': 'Id'})
    def delete(self, id):
        CourseService.delete_by_id(id)
        return jsonify(dict(status='Success', id=id))


# TODO: add error handling
# @ns.errorhandler(exception=exceptions.NotFound)
# def course_not_found(error):
#     return jsonify({'message': 'Not found', 'code': '404'})


if __name__ == '__main__':
    app.run()
