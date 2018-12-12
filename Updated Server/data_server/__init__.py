
from flask import Flask
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

#from config import *
'''app.config.from_object('config.settings')'''
app = Flask(__name__)
#app.config.from_object(__name__)
app.config['DEBUG'] = True
app.config['BASE_DIR'] = os.path.dirname(os.path.abspath(__file__))
app.config['DATABASE'] = os.path.join(BASE_DIR, 'images.db')
app.config['SCHEMA'] = os.path.join(BASE_DIR, 'schema.sql')

import data_server
