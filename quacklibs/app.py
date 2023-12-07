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

# Town Level 1
@app.route("/town1", methods=["GET", "POST"])
def town1():
    # When the method is post
    if request.method == "POST":
        # Create an empty list
        inputs = []
        # Populate the list with all the user inputs from the form
        for key, values in request.form.items():
            # Make sure value exists/that the user put something there
            if not values:
                return 1
            # add value to the list
            inputs.append(values)
        return render_template("town1_done.html", inputs=inputs)
    
    return render_template("town1.html")

# Disney Level 1
@app.route("/disney1", methods=["GET", "POST"])
def disney1():
    if request.method == "POST":
        inputs = []
        for key, values in request.form.items():
            if not values:
                return 1
            inputs.append(values)
        return render_template("disney1_done.html", inputs=inputs)
    
    return render_template("disney1.html")

# Disappearance Level 1
@app.route("/disappearance1", methods=["GET", "POST"])
def disappearance1():
    if request.method == "POST":
        inputs = []
        for key, values in request.form.items():
            if not values:
                return 1
            inputs.append(values)
        return render_template("disappearance1_done.html", inputs=inputs)
    
    return render_template("disappearance1.html")

# Set up the level two page
@app.route("/level2")
def level2():
    return render_template("level2.html")

# Town Level 2
@app.route("/town2", methods=["GET", "POST"])
def town2():
    if request.method == "POST":
        inputs = []

        for key, values in request.form.items():
            if not values:
                return 1
            inputs.append(values)
        print(inputs)
        return render_template("town2_done.html", inputs=inputs)
    
    return render_template("town2.html")

# Disney Level 2
@app.route("/disney2", methods=["GET", "POST"])
def disney2():
    if request.method == "POST":
        inputs = []

        for key, values in request.form.items():
            if not values:
                return 1
            inputs.append(values)
        return render_template("disney2_done.html", inputs=inputs)
    
    return render_template("disney2.html")

# Disappearance Level 2
@app.route("/disappearance2", methods=["GET", "POST"])
def disappearance2():
    if request.method == "POST":
        inputs = []

        for key, values in request.form.items():
            if not values:
                return 1
            inputs.append(values)
        return render_template("disappearance2_done.html", inputs=inputs)
    
    return render_template("disappearance2.html")

# Set up the level three page
@app.route("/level3")
def level3():
    return render_template("level3.html")
# Town Level 3
@app.route("/town3", methods=["GET", "POST"])
def town3():
    if request.method == "POST":
        inputs = []

        for key, values in request.form.items():
            if not values:
                return 1
            inputs.append(values)
        return render_template("town3_done.html", inputs=inputs)
    
    return render_template("town3.html")

# Disney Level 3
@app.route("/disney3", methods=["GET", "POST"])
def disney3():
    if request.method == "POST":
        inputs = []

        for key, values in request.form.items():
            if not values:
                return 1
            inputs.append(values)
        return render_template("disney3_done.html", inputs=inputs)
    
    return render_template("disney3.html")

# Disappearance Level 3
@app.route("/disappearance3", methods=["GET", "POST"])
def disappearance3():
    if request.method == "POST":
        inputs = []

        for key, values in request.form.items():
            if not values:
                return 1
            inputs.append(values)
        return render_template("disappearance3_done.html", inputs=inputs)
    
    return render_template("disappearance3.html")

# Set up the level four page
@app.route("/level4")
def level4():
    return render_template("level4.html")
# Town Level 4
@app.route("/town4", methods=["GET", "POST"])
def town4():
    if request.method == "POST":
        inputs = []

        for key, values in request.form.items():
            if not values:
                return 1
            inputs.append(values)
        return render_template("town4_done.html", inputs=inputs)
    
    return render_template("town4.html")

# Disney Level 4
@app.route("/disney4", methods=["GET", "POST"])
def disney4():
    if request.method == "POST":
        inputs = []

        for key, values in request.form.items():
            if not values:
                return 1
            inputs.append(values)
        return render_template("disney4_done.html", inputs=inputs)
    
    return render_template("disney4.html")

# Disappearance Level 4
@app.route("/disappearance4", methods=["GET", "POST"])
def disappearance4():
    if request.method == "POST":
        inputs = []

        for key, values in request.form.items():
            if not values:
                return 1
            inputs.append(values)
        return render_template("disappearance4_done.html", inputs=inputs)
    
    return render_template("disappearance4.html")

# Set up the level five page
@app.route("/level5")
def level5():
    return render_template("level5.html")
# Town Level 5
@app.route("/town5", methods=["GET", "POST"])
def town5():
    if request.method == "POST":
        inputs = []

        for key, values in request.form.items():
            if not values:
                return 1
            inputs.append(values)
        return render_template("town5_done.html", inputs=inputs)
    
    return render_template("town5.html")

# Disney Level 5
@app.route("/disney5", methods=["GET", "POST"])
def disney5():
    if request.method == "POST":
        inputs = []

        for key, values in request.form.items():
            if not values:
                return 1
            inputs.append(values)
        return render_template("disney5_done.html", inputs=inputs)
    
    return render_template("disney5.html")

# Disappearance Level 5
@app.route("/disappearance5", methods=["GET", "POST"])
def disappearance5():
    if request.method == "POST":
        inputs = []

        for key, values in request.form.items():
            if not values:
                return 1
            inputs.append(values)
        return render_template("disappearance5_done.html", inputs=inputs)
    
    return render_template("disappearance5.html")