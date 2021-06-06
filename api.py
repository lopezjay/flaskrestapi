# Standard Library Imports
import json

# Third Party Imports
import flask


app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET', 'PUT', 'PATCH', 'POST'])
def root():
    content = flask.request
    response_payload = content.json or content.data.decode('utf-8')
    print(response_payload)
    return flask.jsonify(response_payload)

app.run(host="0.0.0.0")
