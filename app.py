import os

from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from metafunctions import apology, cheating, login_required, SQL

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///sql_data/python101.db")

@app.route("/")
@login_required
def index():
    level = str(db.execute("SELECT level FROM users WHERE id = ?", session["user_id"]))
    level = int(level.replace("[{'level': ", "").replace("}]", ""))
    if (level == 11):
        return redirect("/problem-c")
    elif (level == 12):
        return redirect("problem-d")
    else:
        page = "/" + str(level)
        return redirect(page)
    
@app.route("/1", methods=["GET", "POST"])
@login_required
def one():
    if request.method == "POST":
        db.execute("UPDATE users SET level = 2 WHERE id = ?", session["user_id"]) 
        return redirect("/2")
    else:
        return render_template("1.html")
    
@app.route("/2", methods=["GET", "POST"])
@login_required
def two():
    level = str(db.execute("SELECT level FROM users WHERE id = ?", session["user_id"]))
    level = int(level.replace("[{'level': ", "").replace("}]", ""))
    if (level < 2):
        return cheating("Bad request", 400)
    
    if request.method == "POST":
        db.execute("UPDATE users SET level = 3 WHERE id = ?", session["user_id"]) 
        return redirect("/3")
    else:
        return render_template("2.html")
    
@app.route("/3", methods=["GET", "POST"])
@login_required
def three():
    level = str(db.execute("SELECT level FROM users WHERE id = ?", session["user_id"]))
    level = int(level.replace("[{'level': ", "").replace("}]", ""))
    if (level < 3):
        return cheating("Bad request", 400)
    
    if request.method == "POST":
        db.execute("UPDATE users SET level = 4 WHERE id = ?", session["user_id"]) 
        return redirect("/4")
    else:
        return render_template("3.html")
    
@app.route("/4", methods=["GET", "POST"])
@login_required
def four():
    level = str(db.execute("SELECT level FROM users WHERE id = ?", session["user_id"]))
    level = int(level.replace("[{'level': ", "").replace("}]", ""))
    if (level < 4):
        return cheating("Bad request", 400)
        
    if request.method == "POST":
        return redirect("/problem-a")
    else:
        return render_template("4.html")
    
@app.route("/problem-a", methods=["GET", "POST"])
@login_required
def problem_a():
    level = str(db.execute("SELECT level FROM users WHERE id = ?", session["user_id"]))
    level = int(level.replace("[{'level': ", "").replace("}]", ""))
    if (level < 4):
        return cheating("Bad request", 400)
        
    if request.method == "POST":
        db.execute("UPDATE users SET level = 5 WHERE id = ?", session["user_id"]) 
        return redirect("/5")
    else:
        return render_template("problema.html")
    
@app.route("/5", methods=["GET", "POST"])
@login_required
def five():
    level = str(db.execute("SELECT level FROM users WHERE id = ?", session["user_id"]))
    level = int(level.replace("[{'level': ", "").replace("}]", ""))
    if (level < 5):
        return cheating("Bad request", 400)
    
    if request.method == "POST":
        db.execute("UPDATE users SET level = 6 WHERE id = ?", session["user_id"]) 
        return redirect("/6")
    else:
        return render_template("5.html")
    
@app.route("/6", methods=["GET", "POST"])
@login_required
def six():
    level = str(db.execute("SELECT level FROM users WHERE id = ?", session["user_id"]))
    level = int(level.replace("[{'level': ", "").replace("}]", ""))
    if (level < 6):
        return cheating("Bad request", 400)
    
    if request.method == "POST":
        db.execute("UPDATE users SET level = 7 WHERE id = ?", session["user_id"]) 
        return redirect("/7")
    else:
        return render_template("6.html")
    
@app.route("/7", methods=["GET", "POST"])
@login_required
def seven():
    level = str(db.execute("SELECT level FROM users WHERE id = ?", session["user_id"]))
    level = int(level.replace("[{'level': ", "").replace("}]", ""))
    if (level < 7):
        return cheating("Bad request", 400)
    
    if request.method == "POST":
        return redirect("/problem-b")
    else:
        return render_template("7.html")
    
@app.route("/problem-b", methods=["GET", "POST"])
@login_required
def problem_b():
    level = str(db.execute("SELECT level FROM users WHERE id = ?", session["user_id"]))
    level = int(level.replace("[{'level': ", "").replace("}]", ""))
    if (level < 7):
        return cheating("Bad request", 400)
        
    if request.method == "POST":
        db.execute("UPDATE users SET level = 8 WHERE id = ?", session["user_id"]) 
        return redirect("/8")
    else:
        return render_template("problemb.html")
    
@app.route("/8", methods=["GET", "POST"])
@login_required
def eight():
    level = str(db.execute("SELECT level FROM users WHERE id = ?", session["user_id"]))
    level = int(level.replace("[{'level': ", "").replace("}]", ""))
    if (level < 8):
        return cheating("Bad request", 400)
        
    if request.method == "POST":
        db.execute("UPDATE users SET level = 9 WHERE id = ?", session["user_id"]) 
        return redirect("/9")
    else:
        return render_template("8.html")
    
@app.route("/9", methods=["GET", "POST"])
@login_required
def nine():
    level = str(db.execute("SELECT level FROM users WHERE id = ?", session["user_id"]))
    level = int(level.replace("[{'level': ", "").replace("}]", ""))
    if (level < 9):
        return cheating("Bad request", 400)
    
    if request.method == "POST":
        db.execute("UPDATE users SET level = 10 WHERE id = ?", session["user_id"]) 
        return redirect("/10")
    else:
        return render_template("9.html")
    
@app.route("/10", methods=["GET", "POST"])
@login_required
def ten():
    level = str(db.execute("SELECT level FROM users WHERE id = ?", session["user_id"]))
    level = int(level.replace("[{'level': ", "").replace("}]", ""))
    if (level < 10):
        return cheating("Bad request", 400)
    
    if request.method == "POST":
        db.execute("UPDATE users SET level = 11 WHERE id = ?", session["user_id"]) 
        return redirect("/problem-c")
    else:
        return render_template("10.html")
    
@app.route("/problem-c", methods=["GET", "POST"])
@login_required
def problem_c():
    level = str(db.execute("SELECT level FROM users WHERE id = ?", session["user_id"]))
    level = int(level.replace("[{'level': ", "").replace("}]", ""))
    if (level < 11):
        return cheating("Bad request", 400)
    
    if request.method == "POST":
        db.execute("UPDATE users SET level = 12 WHERE id = ?", session["user_id"]) 
        return redirect("/problem-d")
    else:
        return render_template("problemc.html")

@app.route("/problem-d")
@login_required
def problem_d():
    level = str(db.execute("SELECT level FROM users WHERE id = ?", session["user_id"]))
    level = int(level.replace("[{'level': ", "").replace("}]", ""))
    if (level < 12):
        return cheating("Bad request", 400)
    return render_template("problemd.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""
    session.clear()
    
    if request.method == "POST":
        
        if not request.form.get("username"):
            return apology("Must provide username", 403)
        elif not request.form.get("password"):
            return apology("Must provide password", 403)

        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("Invalid username and/or password", 403)
            
        session["user_id"] = rows[0]["id"]
        flash("Logged in!")
        return redirect("/")
        
    else:
        return render_template("login.html")
        
@app.route("/leaderboard")
def leaderboard():
    users = db.execute("SELECT * FROM users")
    return render_template("leaderboard.html", users=users)

@app.route("/logout")
def logout():
    """Log user out"""
    session.clear()
    
    return redirect("/")
    flash("Logged out!")

@app.route("/register", methods=["GET", "POST"])
def register():
    
    session.clear()
    
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        rows = db.execute("SELECT * FROM users WHERE username = ?", username)

        if not username:
            return apology("Please provide a username.", 400)
        elif not password:
            return apology("Please provide a password.", 400)
        elif len(rows) != 0:
            return apology("This username already exists.", 400)
        elif not request.form.get("confirmation"):
            return apology("Please provide a confirmation password.", 400)
        elif password != confirmation:
            return apology("Your password must match the confirmation.", 400)
        else:
            hash2 = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
            db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, hash2)
            flash("Registered!")
            return redirect("/")
    else:
        return render_template("register.html")


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


for code in default_exceptions:
    app.errorhandler(code)(errorhandler)

# Created by Ethan Ali