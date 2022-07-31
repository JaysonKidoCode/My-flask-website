from flask import Blueprint

views = Blueprint('views', _name_)

@views.route('/')
def home():
    return "<h1>Test</h1>"