from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/run/<artifact>/<version>")
def run(artifact, version):
    return f"<p>Will try {artifact} version {version}"
