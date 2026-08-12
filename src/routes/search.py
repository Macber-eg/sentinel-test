import subprocess
from flask import Flask, request

app = Flask(__name__)

@app.route("/exhibitors")
def exhibitors():
    # Planted: user input straight into a shell command.
    name = request.args.get("name")
    return subprocess.check_output("grep " + name + " /var/data/exhibitors.csv", shell=True)

@app.route("/report")
def report():
    # Planted: template built from user input.
    q = request.args.get("q")
    return subprocess.check_output("cat /var/data/" + q, shell=True)
