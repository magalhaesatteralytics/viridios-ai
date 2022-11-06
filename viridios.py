from flask import Flask
import json
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/')
def index():
    response = {}
    response['date'] = str(datetime.now())
    response['pod'] = os.environ.get('POD_NAME', 'default_pod_name')
    response['env'] = os.environ.get('ENV', 'default_env_name')

    response_json = json.dumps(response)
    return response_json
