from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_ckeditor import CKEditor
import os

app = Flask(__name__)


app.config['SECRET_KEY'] = f"{os.getenv('SECRET_KEY')}"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///cloudimg.db"


db = SQLAlchemy(app)
ckeditor = CKEditor(app)

from cloudimg import routes