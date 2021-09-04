from datetime import datetime
from typing import List

from course.models import CourseModel as Course
from course.schemas import course_schema, courses_schema
from db import db


class CourseService:
    @staticmethod
    def get_all(**kwargs) -> List[Course]:
        """
        Method that filters courses by name and start date.
        There is an upper and lower limit for the start date.
        If there are no filters, a list of all courses is returned.
        :param kwargs: filter params (name, upper and lower limit for start_date
        :return: List of courses.
        """
        courses = Course.query
        if "name" in kwargs:
            courses = courses.filter(Course.name == kwargs["name"])
        if "start_more" in kwargs:
            courses = courses.filter(
                Course.start_date >= CourseService._convert_date(kwargs["start_more"])
            )
        if "start_less" in kwargs:
            courses = courses.filter(
                Course.start_date <= CourseService._convert_date(kwargs["start_less"])
            )
        return courses_schema.jsonify(courses.all())

    @staticmethod
    def get_by_id(course_id: int) -> Course:
        """
        Search course in the database by id.
        :param course_id: unique course identifier
        :return: course obj or error 404
        """
        course = Course.query.filter(Course.id == course_id).first_or_404()
        return course_schema.jsonify(course)

    @staticmethod
    def update(id, request) -> Course:
        """
        Method that updates the course by new data.
        :param id: unique course identifier
        :param request: new data
        :return: updated course
        """
        new_data = course_schema.loads(request.data)
        course = (
            db.session.query(Course)
            .filter_by(id=id)
            .update(CourseService._prepare_data(new_data))
        )
        db.session.commit()
        return course_schema.jsonify(course)

    @staticmethod
    def delete_by_id(course_id: int) -> int:
        """
        Method that removes the course from the database.
        :param course_id:
        :return: deleted course id
        """
        course = Course.query.filter(Course.id == course_id).first_or_404()
        db.session.delete(course)
        db.session.commit()
        return course_id

    @staticmethod
    def create(request) -> Course:
        """
        Method that creates a new course and adds it to the database.
        :param request: new course data
        :return: created course
        """
        new_course = course_schema.loads(request.data)
        db.session.add(Course(**new_course))
        db.session.commit()
        return course_schema.jsonify(new_course)

    @staticmethod
    def _prepare_data(data):
        if "start_date" in data:
            data["start_date"] = CourseService._convert_date(data["start_date"])
        if "end_date" in data:
            data["end_date"] = CourseService._convert_date(data["end_date"])
        return data

    @staticmethod
    def _convert_date(date_string):
        """
        Method that converts a string to a python date
        :param date_string: date in string format
        :return: date in python datetime format
        """
        return datetime.strptime(date_string, "%d-%m-%y")
