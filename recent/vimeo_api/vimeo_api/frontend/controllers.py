from flask import Blueprint, render_template

frontend = Blueprint('frontend', __name__, url_prefix='/vimeo')


@frontend.route('/', methods=['GET'])
def index():
    """Renders the index page"""
    return render_template('frontend/index.html')
