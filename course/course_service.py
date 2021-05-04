from datetime import datetime
from typing import List

from course.course_model import CourseModel as Course
from course.course_schema import course_schema, courses_schema
from db import db


class CourseService:
    @staticmethod
    def get_all(**kwargs) -> List[Course]:
        courses = Course.query
        if 'name' in kwargs:
            courses = courses.filter(Course.name == kwargs['name'])
        if 'start_more' in kwargs:
            courses = courses.filter(Course.start_date >= CourseService._convert_date(kwargs['start_more']))
        if 'start_less' in kwargs:
            courses = courses.filter(Course.start_date <= CourseService._convert_date(kwargs['start_less']))
        return courses_schema.jsonify(courses.all())

    @staticmethod
    def get_by_id(course_id: int) -> Course:
        course = Course.query.filter(Course.id == course_id).first_or_404()
        return course_schema.jsonify(course)

    @staticmethod
    def update(id, request) -> Course:
        new_data = course_schema.loads(request.data)
        course = db.session.query(Course).filter_by(id=id).update(CourseService._prepare_data(new_data))
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
        new_course = course_schema.loads(request.data)
        db.session.add(Course(**new_course))
        db.session.commit()
        return course_schema.jsonify(new_course)

    @staticmethod
    def _prepare_data(data):
        if 'start_date' in data:
            data['start_date'] = CourseService._convert_date(data['start_date'])
        if 'end_date' in data:
            data['end_date'] = CourseService._convert_date(data['end_date'])
        return data

    @staticmethod
    def _convert_date(date_string):
        return datetime.strptime(date_string, '%d-%m-%y')
