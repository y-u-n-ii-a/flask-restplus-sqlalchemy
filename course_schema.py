from marshmallow import Schema, fields


class CourseSchema(Schema):
    id = fields.Number(attribute='id')
    name = fields.String(attribute='name')
    start_date = fields.Date(attribute='start_date')
    end_date = fields.Date(attribute='end_date')
    number_of_lectures = fields.Number(attribute='number_of_lectures')
