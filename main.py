from flask import Blueprint, render_template
from flask_login import current_user

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
def homepage():
    return render_template('index.html', user=current_user)