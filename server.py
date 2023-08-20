import argparse
import os

import numpy as np
import pandas as pd

from flask import Flask
from flask_cors import CORS
from flask_restful import Resource
from flask_restful import Api
from flask import jsonify, make_response, send_file

cwd = os.getcwd()


class GetHelp(Resource):

    def get(self, 
            emotion, 
            ):

        response = ""
        # if emotion == 1:
        #     response = "Calm down"
        # elif emotion == 2:
        #     response = "Don't worry"
        # elif emotion == 3:
        #     response = "You are okay"
        # elif emotion == 4:
        #     response = "You are fine"
        # elif emotion == 5:
        #     response = "You are fine"
        # elif emotion == 6:
        #     response = "Do something fun"
        # elif emotion == 7:
        #     response = "You are fine"

        if emotion == "Angry":
            response = "Calm down"
        elif emotion == "Disgust":
            response = "Don't worry"
        elif emotion == "Fear":
            response = "You are okay"
        elif emotion == "Happy":
            response = "You are fine"
        elif emotion == "Neutral":
            response = "You are fine"
        elif emotion == "Sad":
            response = "Do something fun"
        elif emotion == "Surprise":
            response = "You are fine"

        

        return jsonify({
            'result': response
        })


def create_app():
    app = Flask(__name__)  # static_url_path, static_folder, template_folder...
    CORS(app, resources={r"/*": {"origins": "*"}})
    api = Api(app)

    api.add_resource(GetHelp, "/api/<string:emotion>")

    @app.route('/version')
    def version():
        return f"Job ID: {os.environ['JOB_ID']}\nCommit ID: {os.environ['COMMIT_ID']}"

    return app


def start_server():
    print("Starting server...")
    parser = argparse.ArgumentParser()

    # API flag
    parser.add_argument(
        "--host",
        default="127.0.0.1",
        help="The host to run the server",
    )
    parser.add_argument(
        "--port",
        default=8000,
        help="The port to run the server",
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Run Flask in debug mode",
    )

    args = parser.parse_args()

    server_app = create_app()

    server_app.run(debug=args.debug, host=args.host, port=args.port)


if __name__ == "__main__":
    start_server()
