"""하나의 블류프린트 인듯"""

import json
import random
import time
from datetime import datetime
from flask import (
    Blueprint, flash, g, redirect,
    render_template, request, url_for, Response
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('laser11', __name__)


@bp.route('/')
def index():
    db = get_db()
    posts = db.execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
    # return render_template('laser/index.html', posts=posts)
    # return render_template('laser/chart2.html', posts=posts)
    return render_template('laser11/chart2.html', posts=posts)


@bp.route('/chart-data')
def chart_data():
    def generate_random_data():
        while True:
            # now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            now = datetime.now().strftime('%H:%M:%S-%f')
            json_data = json.dumps({'time': now, 'value': random.random() * 10})
            yield f"data:{json_data}\n\n"
            time.sleep(0.2)  #

    return Response(generate_random_data(), mimetype='text/event-stream')
