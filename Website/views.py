from flask import Blueprint, render_template
from os.path import join, split

DIRECTORY = split(__file__)[0]

views = Blueprint('views', __name__)

@views.route('/')
def home():
    #return render_template(join(DIRECTORY, 'templates', 'index.html'))

    return render_template("test.html")