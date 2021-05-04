from flask import request, jsonify
from flask_restplus import Namespace, Resource, fields

from course.course_service import CourseService

ns = Namespace('course', description='Course operations')

course_expected_model = ns.model('Course', {
    'id': fields.Integer(readonly=True),
    'name': fields.String(),
    'start_date': fields.Date(),
    'end_date': fields.Date(),
    'number_of_lectures': fields.Integer
})


@ns.route('/')
class CourseListResource(Resource):
    @ns.doc('Get list of courses with filter')
    def get(self):
        # TODO: fix filters
        return CourseService.get_all(name=request.args.get('name'))

    @ns.doc('Add new course')
    @ns.expect(course_expected_model)
    def post(self):
        return CourseService.create(request)


@ns.route('/<int:id>')
@ns.param('id', 'The course identifier')
class CourseResource(Resource):
    @ns.doc('Get course by id')
    def get(self, id: int):
        return CourseService.get_by_id(id)

    @ns.doc('Change the course')
    @ns.expect(course_expected_model)
    def put(self, id: int):
        CourseService.update(id, request)

    @ns.doc('Delete course by id')
    def delete(self, id: int):
        CourseService.delete_by_id(id)
        return jsonify(dict(status='Success', id=id))
