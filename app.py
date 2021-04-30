from flask import Flask
from flask_restplus import Api

from course.course_controller import ns as course_ns
from db import db
from ma import ma

app = Flask(__name__)
app.config.from_pyfile('config.py')

api = Api(app)
api.add_namespace(course_ns)


@app.before_first_request
def create_tables():
    db.create_all()


db.init_app(app)
ma.init_app(app)

if __name__ == '__main__':
    app.run()
# TODO: add unittests
