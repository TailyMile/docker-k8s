from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics
import time
import random

app = Flask(__name__)
metrics = PrometheusMetrics(app)


@app.route('/')
def main():
    time.sleep(random.random() * 0.2)
    return 'Hello World!'