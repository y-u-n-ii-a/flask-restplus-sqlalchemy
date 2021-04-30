from datetime import datetime

from db import db


class CourseModel(db.Model):
    __tablename__ = 'course'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    number_of_lectures = db.Column(db.Integer)

    def __init__(self, name, start_date, end_date, number_of_lectures):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.number_of_lectures = number_of_lectures

    def __repr__(self):
        return '<Course %r>' % self.id

    # TODO: correct serialization
    def serialize(self):
        return {'name': self.name,
                'start_date': self.start_date,
                'end_date': self.end_date,
                'number_of_lectures': self.number_of_lectures
                }


def deserialize(request):
    name = request.json['name']
    start_date = datetime.strptime(request.json['start_date'], '%d/%m/%y')
    end_date = datetime.strptime(request.json['end_date'], '%d/%m/%y')
    number_of_lectures = request.json['number_of_lectures']
    return CourseModel(name, start_date, end_date, number_of_lectures)


def serialize_list(courses):
    courses_list = {}
    for course in courses:
        courses_list['Course %r' % course.id] = course.serialize()
    return courses_list