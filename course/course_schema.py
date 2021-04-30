from ma import ma


class CourseSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'start_date', 'end_date', 'number_of_lectures')


course_schema = CourseSchema()
courses_schema = CourseSchema(many=True)
