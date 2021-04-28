from flask import Flask, request, jsonify
from flask_restplus import Api, Resource, fields
from db import db
from course_service import CourseModel

app = Flask(__name__)
app.config.from_pyfile('config.py')

api = Api(app)
db.init_app(app)


course_model = api.model('Course', {
    'id': fields.Integer(readonly=True),
    'name': fields.String(),
    # 'start_date': fields.Date(),
    # 'end_date': fields.Date(),
    'number_of_lectures': fields.Integer
})


@api.route('/course')
class CourseList(Resource):
    @api.doc('Get list of courses')
    def get(self):
        all_courses = db.session.query(CourseModel).first()
        return jsonify(all_courses.serialize())

    @api.doc('Delete all courses')
    def delete(self):
        db.session.query(CourseModel).delete()
        db.session.commit()
        return 200

    @api.doc('Add new course')
    @api.expect(course_model)
    def post(self):
        name = request.json['name']
        # start_date = request.json['start_date']
        # end_date = request.json['end_date']
        number_of_lectures = request.json['number_of_lectures']

        new_course = CourseModel(name, number_of_lectures)
        db.session.add(new_course)
        db.session.commit()
        pass


# TODO: handle error if the element doesn't exist
@api.route('/course/<int:id>')
class Course(Resource):
    @api.doc('Get course by id', params={'id': 'Id'})
    def get(self, id):
        course = db.session.query(CourseModel).get(id)
        return jsonify(course.serialize())

    @api.doc('Change course', params={'id': 'Id'})
    @api.expect(course_model)
    def put(self, id):
        course = CourseModel.query.get(id)

        course.name = request.json['name']
        # course.start_date = request.json['start_date']
        # course.end_date = request.json['end_date']
        course.number_of_lectures = request.json['number_of_lectures']

        db.session.commit()
        pass

    @api.doc('Delete course by id', params={'id': 'Id'})
    def delete(self, id):
        db.session.query(CourseModel).filter(CourseModel.id == id).delete()
        db.session.commit()

        return 200


if __name__ == '__main__':
    app.run()
