from flask import request, g, redirect, url_for, abort, render_template, send_from_directory
import time
import os
import sqlite3
from hashlib import md5
from PIL import Image
from werkzeug.utils import secure_filename
from . import app


def connect_db():
    """ Connect to the SQLite database.
    """
    query = open(app.config['SCHEMA'], 'r').read()
    conn = sqlite3.connect(app.config['DATABASE'])
    cursor = conn.cursor()
    cursor.executescript(query)
    conn.commit()
    cursor.close()
    return sqlite3.connect(app.config['DATABASE'])

def check_extension(extension):
    return extension in app.config['ALLOWED_EXTENSIONS']

def get_last_reqs():
    """ Return a list of the last 25 uploaded images
    """
    cur = g.db.execute('select filename from data order by created_on desc limit 25')
    req = [row[0] for row in cur.fetchall()]
    return req

def add_data(req):
    """ Insert filename into database
    """
    g.db.execute('insert into data (reqdata) values (?)', [req])
    g.db.commit()

@app.before_request
def before_request():
    """ Executes before each request.
    Taken from flask example app
    """
    g.db = connect_db()

@app.teardown_request
def teardown_request(err):
    """ Executes after each request, regardless of whether
    there was an exception or not.
    """
    if err:
        app.logger.info(err.message)
    database = getattr(g, 'db', None)
    if database is not None:
        database.close()

@app.errorhandler(404)
def page_not_found(err):
    """ Redirect to 404 on error.
    """
    if err:
        app.logger.info(err.message)
    return render_template('404.html'), 404

@app.route('/', methods=['GET', 'POST'])
def upload_data():
    """ Default route.
    """
    if request.method == 'POST':
		print request.data
		import ast
		request.data = ast.literal_eval(request.data)
		multi_dict = request.args
		'''for key in multi_dict:
			print multi_dict.get(key)
			print multi_dict.getlist(key)'''	
		name = request.data['name']
		numPeople=request.data['numPeople']
		special= request.data['special']
		f = "name:"+name+" No of people: "+ numPeople + "Special: "+special 
		print f	
		add_data(f)
return "ok"
