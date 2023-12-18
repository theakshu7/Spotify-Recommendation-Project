from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import json
import bonsai_query

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return "Landing route for flask backend."

@app.route("/data", methods=['GET', 'POST'])
def data():
    if request.method == "POST":
        data = request.get_json()
        track_uri_json = json.dumps(data, indent=4)
        with open("track_uri.json", "w") as output:
            output.write(track_uri_json)
        print(data)
        tracks_uris, mood = bonsai_query.get_track_ids()
        return tracks_uris, mood
    else:
        return "Hello world"


if __name__ == "__main__":
    app.run()
