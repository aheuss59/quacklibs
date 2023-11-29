from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session

# Configure application
app = Flask(__name__) 

# Render the homepage
@app.route("/")
def index():
    return render_template("index.html")

# Set up the level one page
@app.route("/level1")
def level1():
    return render_template("level1.html")

# Set up the level two page
@app.route("/level2")
def level2():
    return render_template("level2.html")

# Set up the level three page
@app.route("/level3")
def level3():
    return render_template("level3.html")