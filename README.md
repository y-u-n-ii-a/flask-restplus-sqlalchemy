# REST API With Flask & SQL Alchemy

> Products API using Python Flask, SQLAlchemy and Flask-RESTPlus

## Quick Start
#### Clone the Project

``` bash
$ git clone https://github.com/y-u-n-ii-a/flask-restplus-server-example.git
```

#### Setup Environment

You will need `invoke` package to work with everything related to this project.

``` bash
$ pip install -r requirements.txt
```

#### Create DB
``` bash
$ python
>> from app import db
>> db.create_all()
>> exit()
```

#### Run Server (http://127.0.0.1:5000)
``` bash
$ python app.py
```

## Endpoints

* GET     /course
* GET     /course/:id
* POST    /course
* PUT     /course/:id
* DELETE  /course
* DELETE  /course/:id