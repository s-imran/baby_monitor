#!flask/bin/python
import os
import json
from flask import Flask, jsonify, request, abort
from collections import defaultdict
from typing import Dict

app = Flask(__name__)


def load_db(db_path: str) -> Dict[str, str]:
    if os.path.getsize(db_path) > 0:
        with open(db_path, "r") as _f:
            db_json = json.load(_f)
            return defaultdict(str, db_json)
    else:
        return defaultdict(str)


def write_db(db_path: str, client_dict) -> None:
    with open(db_path, "w") as _f:
        json.dump(client_dict, _f)


@app.route('/baby_monitor/api/v1.0/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'phone_id' in request.json:
        abort(400)

    phone_id = request.json.get("phone_id")
    token = request.json.get("token")
    client_dict = load_db(os.environ["DB_PATH"])
    client_dict[phone_id] = token
    write_db(os.environ["DB_PATH"], client_dict)

    return jsonify({"phone_id": phone_id, "token": token}), 201


if __name__ == '__main__':
    app.run(debug=True)
