import subprocess
from flask import Flask, request

app = Flask(__name__)

@app.route("/backup")
def backup():
    # Planted: user input straight into a shell command.
    target = request.args.get("target")
    return subprocess.check_output("tar czf /tmp/b.tgz " + target, shell=True)
