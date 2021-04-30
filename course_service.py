from typing import List

from course_model1 import CourseModel as Course, deserialize
from db import db


class CourseService:
    @staticmethod
    def get_all() -> List[Course]:
        return Course.query.all()

    @staticmethod
    def get_by_id(course_id: int) -> Course:
        return Course.query.get(course_id).serialize()

    # @staticmethod
    # def update(course: Course, course_change_updates: courseInterface) -> course:
    #     course.update(course_change_updates)
    #     db.session.commit()
    #     return course

    @staticmethod
    def delete_by_id(course_id: int) -> List[int]:
        course = Course.query.filter(Course.id == course_id).first_or_404()
        if not course:
            return []
        db.session.delete(course)
        db.session.commit()
        return [course_id]

    @staticmethod
    def create(request) -> Course:
        new_course = deserialize(request)
        db.session.add(new_course)
        db.session.commit()
        # except:
        #     return abort(400)
        return new_course
