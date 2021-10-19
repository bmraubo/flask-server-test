import re
from flask import Flask, request
import os

app = Flask(__name__)


def reverse_string(string):
    return string[::-1]


@app.route("/", methods=["GET", "POST"])
def index():
    return "Hello World"


@app.route("/post-test", methods=["POST"])
def process_JSON():
    request_data = request.get_json()
    extracted_name = reverse_string(request_data["name"])
    response_data = {"message": "Hello " + extracted_name}
    return response_data, 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
