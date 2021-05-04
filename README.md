# REST API With Flask & SQL Alchemy

> Simple API using Python Flask, SQLAlchemy, Marshmallow and Flask-RESTPlus

## Quick Start
#### Clone the Project

``` bash
$ git clone https://github.com/y-u-n-ii-a/flask-restplus-sqlalchemy.git
```

#### Setup Environment

Create virtual environment using pyenv, virtualenv or the same utility.
For linux (ubuntu) you can use:
``` bash
$ sudo apt install python3-venv
$ python3 -m venv venv
```

Activate venv and install the project:
``` bash
$ source venv/bin/activate
$ python -m pip install -e
```

#### Install requirements:

``` bash
$ pip install -r requirements.txt
```


#### Run Server (http://127.0.0.1:5000)
``` bash
$ flask run
```

## Endpoints

* GET     /course
* GET     /course/:id
* POST    /course
* PUT     /course/:id
* DELETE  /course/:id

## Request with filter (example):
http://127.0.0.1:5000/course/?name=yuniia&start_more=01-01-01&start_less=02-02-02

Be attentive, you need to use date format 'dd-mm-yy'.