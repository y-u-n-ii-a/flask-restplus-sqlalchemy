# import os
#
# basedir = os.path.dirname(__file__)

DEBUG = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///courses.db'
# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'courses.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
