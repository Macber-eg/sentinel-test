import sqlite3
from flask import Flask, request

app = Flask(__name__)

@app.route("/report")
def report():
    # Planted: user input concatenated straight into SQL.
    name = request.args.get("name")
    con = sqlite3.connect("/var/data/app.db")
    return str(con.execute("SELECT id FROM exhibitors WHERE name = '" + name + "'").fetchall())
