from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session

# Configure application
app = Flask(__name__) 

db = SQL("sqlite:///libs.db")

# Define a function that can get the number of inputs needed for a lib and loop through to get user input
# This makes the code a bit less redundant

# Render the homepage
@app.route("/")
def index():
    return render_template("index.html")

# Set up the level one page
@app.route("/level1")
def level1():
    return render_template("level1.html")

# Town Level 1
@app.route("/town1", methods=["GET", "POST"])
def town1():
    if request.method == "POST":
        word1 = request.form.get("1")
        print(word1)
        return render_template("town1_done.html")
    return render_template("town1.html")
    


# Disney Level 1
@app.route("/disney1", methods=["GET", "POST"])
def disney1():
    if request.method == "POST":
        inputs = collect("disney1")
        return render_template("disney1_done.html", inputs=inputs)
    
    return render_template("disney1.html")

# Set up the level two page
@app.route("/level2")
def level2():
    return render_template("level2.html")

# Town Level 2
@app.route("/town2", methods=["GET", "POST"])
def town2():
    if request.method == "POST":
        inputs = collect("town2")
        return render_template("town2_done.html", inputs=inputs)
    
    return render_template("town2.html")

# Disney Level 2
@app.route("/disney2", methods=["GET", "POST"])
def disney2():
    if request.method == "POST":
        inputs = collect("disney2")
        return render_template("disney2_done.html", inputs=inputs)
    
    return render_template("disney2.html")

# Set up the level three page
@app.route("/level3")
def level3():
    return render_template("level3.html")
# Town Level 3
@app.route("/town3", methods=["GET", "POST"])
def town3():
    if request.method == "POST":
        inputs = collect("town3")
        return render_template("town3_done.html", inputs=inputs)
    
    return render_template("town3.html")

# Disney Level 3
@app.route("/disney3", methods=["GET", "POST"])
def disney3():
    if request.method == "POST":
        inputs = collect("disney3")
        return render_template("disney3_done.html", inputs=inputs)
    
    return render_template("disney3.html")