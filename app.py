from datetime import datetime

from flask import Flask, request, jsonify, abort
from flask_restplus import Api, Resource, fields

from course_service import CourseModel, serialize_list, deserialize
from db import db

app = Flask(__name__)
app.config.from_pyfile('config.py')


@app.before_first_request
def create_tables():
    db.create_all()


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
class CourseList(Resource):
    @ns.doc('Get list of courses')
    def get(self):
        courses_list = []
        courses_list.extend(db.session.query(CourseModel).all())
        return jsonify(serialize_list(courses_list))

    @ns.doc('Add new course')
    @ns.expect(course_model)
    def post(self):
        try:
            new_course = deserialize(request)
            db.session.add(new_course)
            db.session.commit()
            pass
        except:
            return abort(400)


# TODO: handle error if the element doesn't exist
@ns.route('/<int:id>')
class Course(Resource):
    @ns.doc('Get course by id', params={'id': 'Id'})
    def get(self, id):
        course = db.session.query(CourseModel).get(id)
        if course is not None:
            return jsonify(course.serialize())
        else:
            abort(404)

    @ns.doc('Change course', params={'id': 'Id'})
    @ns.expect(course_model)
    def put(self, id):
        course = CourseModel.query.get(id)

        # TODO: provide for the addition of not all fields
        course.name = request.json['name']
        course.start_date = datetime.strptime(request.json['start_date'], '%d/%m/%y')
        course.end_date = datetime.strptime(request.json['end_date'], '%d/%m/%y')
        course.number_of_lectures = request.json['number_of_lectures']

        db.session.commit()
        return jsonify(
            message=f"Course #{id} updated successfully.",
            category="success",
            status=200
        )

    @ns.doc('Delete course by id', params={'id': 'Id'})
    def delete(self, id):
        db.session.query(CourseModel).filter(CourseModel.id == id).delete()
        db.session.commit()

        return jsonify(
            message=f"Course #{id} deleted successfully.",
            category="success",
            status=200
        )


#
# @ns.errorhandler(exception=exceptions.NotFound)
# def course_not_found(error):
#     return jsonify({'message': 'Not found', 'code': '404'})


if __name__ == '__main__':
    app.run()
