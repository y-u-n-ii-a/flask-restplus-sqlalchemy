# basedir = os.path.dirname(__file__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'courses.sqlite')

DEBUG = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///courses.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
