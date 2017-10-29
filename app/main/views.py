from flask import render_template, session, current_app, redirect, url_for

from app import db
from app.auth.forms import LoginForm
from app.models import User
from . import main


@main.route('/')
def index():
    return render_template('index.html')
