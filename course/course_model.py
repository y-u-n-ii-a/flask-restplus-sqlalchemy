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
