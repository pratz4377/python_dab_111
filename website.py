from flask import Flask, render_template
import sqlite3 as sql
import json


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/data")
def data():

    conn = sql.connect("salary")
    conn.row_factory = sql.Row
    c = conn.cursor()
    c.execute("select * from salaries")
    
    columns = [column[0] for column in c.description]
    result_list = [dict(zip(columns, row)) for row in c.fetchall()]
    jsonData = json.dumps(result_list)
   
   
    return render_template("data.html",jsonData=jsonData)


@app.route("/about")
def about_page():
    return render_template("about.html")