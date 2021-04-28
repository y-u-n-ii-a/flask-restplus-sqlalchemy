from flask import Flask, request, jsonify
from flask_restplus import Api, Resource, fields
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.py')

api = Api(app)
db = SQLAlchemy(app)


class CourseModel(db.Model):
    __tablename__ = 'course'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    number_of_lectures = db.Column(db.Integer)

    def __init__(self, name, number_of_lectures):
        self.name = name
        # self.start_date = start_date
        # self.end_date = end_date
        self.number_of_lectures = number_of_lectures

    def __repr__(self):
        return '<Course %r>' % self.id

    def serialize(self):
        return {'name': self.name,
                'number_of_lectures': self.number_of_lectures
                }


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
