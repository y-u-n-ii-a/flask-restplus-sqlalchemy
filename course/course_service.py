from datetime import datetime
from typing import List

from sqlalchemy import sql

from course.course_model import CourseModel as Course
from course.course_schema import course_schema, courses_schema
from db import db


class CourseService:
    @staticmethod
    def get_all(**kwargs) -> List[Course]:
        courses = Course.query.filter_by(sql.and_(**kwargs)).all()
        return courses_schema.jsonify(courses)

    @staticmethod
    def get_by_id(course_id: int) -> Course:
        course = Course.query.filter(Course.id == course_id).first_or_404()
        return course_schema.jsonify(course)

    @staticmethod
    def update(id, request) -> Course:
        course = db.session.query(Course).filter(Course.id == id).first_or_404()
        # TODO: provide for the addition of not all fields
        course.name = request.json['name']
        course.start_date = datetime.strptime(request.json['start_date'], '%d/%m/%y')
        course.end_date = datetime.strptime(request.json['end_date'], '%d/%m/%y')
        course.number_of_lectures = request.json['number_of_lectures']
        db.session.commit()
        return course_schema.jsonify(course)

    @staticmethod
    def delete_by_id(course_id: int) -> List[int]:
        course = Course.query.filter(Course.id == course_id).first_or_404()

        db.session.delete(course)
        db.session.commit()
        return [course_id]

    @staticmethod
    def create(request) -> Course:
        name = request.json['name']
        start_date = datetime.strptime(request.json['start_date'], '%d/%m/%y')
        end_date = datetime.strptime(request.json['end_date'], '%d/%m/%y')
        number_of_lectures = request.json['number_of_lectures']

        # new_course = course_schema.load(request)
        new_course = Course(name, start_date, end_date, number_of_lectures)
        db.session.add(new_course)
        db.session.commit()
        return course_schema.jsonify(new_course)
