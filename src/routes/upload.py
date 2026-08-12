import subprocess
from flask import Flask, request

app = Flask(__name__)

@app.route("/extract")
def extract():
    # Planted: user input straight into a shell command.
    archive = request.args.get("archive")
    return subprocess.check_output("tar xzf /uploads/" + archive, shell=True)

// touch to re-trigger the gate now trivy can open its database
