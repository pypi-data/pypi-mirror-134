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
from flaskr import my_globals as g

bp = Blueprint('dashboard', __name__)


@bp.route('/dashboard')
def index():
    return render_template('/dashboard/index.html',
                           title='My Title',
                           message=g.hostname)


# @bp.route('/chart-data-91')
# def chart_data_91():
#     def generate_random_data():
#         while True:
#             # now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#             now = datetime.now().strftime('%H:%M:%S-%f')
#             value = random.random() * 1000
#             json_data = json.dumps({'time': now, 'value': value})
#             yield f"data:{json_data}\n\n"
#             time.sleep(0.2)  #
#     return Response(generate_random_data(), mimetype='text/event-stream')

"""
navbar.py 로 이동하다. 21.1012

@bp.route('/chart-data')
def chart_data():
    def get_data():
        while True:
            now = datetime.now().strftime('%H:%M:%S-%f')  # OR
            # now = g.adc_time[0]
            # value = random.random()*100 # OR
            value = g.adc_data[0]
            json_data = json.dumps({'time': now, 'value': value, 'temp': g.cpu_temp})
            yield f"data:{json_data}\n\n"
            time.sleep(0.2)  #

    return Response(get_data(), mimetype='text/event-stream')
"""
