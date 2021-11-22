import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required

import datetime


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
db = SQL("sqlite:///data.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/")
@login_required
def index():
    # ログインしている人の名前のリストを取り出す[{'username': 'test'}]
    name_dict = db.execute("SELECT username FROM users WHERE id = :id", id=session["user_id"])
    # 名前だけをとりだす
    name = name_dict[0]["username"]
    date_dict = db.execute("SELECT timestamp FROM history WHERE user_id = :id", id=session["user_id"])
    # print(date_dict)
    date_length = len(date_dict)
    # print(date_length)
    # print(date_dict[date_length - 1])
    date = date_dict[date_length - 2]["timestamp"]
    return render_template("index.html", name=name, date = date)


@app.route("/home")
@login_required
def home():
    # ログインしている人の名前のリストを取り出す[{'username': 'test'}]
    name_dict = db.execute("SELECT username FROM users WHERE id=:id", id=session["user_id"])
    # 名前だけをとりだす
    name = name_dict[0]["username"]
    return render_template("index.html", name=name)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]
        db.execute(
                "INSERT INTO history (user_id, timestamp) VALUES (?, ?)",
                session["user_id"],
                datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            )

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/learn", methods=["GET", "POST"])
@login_required
def learn():
    # selectbox用
    # 使わなかった
    word_type_list = ["number", "move"]
    return render_template("learn.html")


@app.route("/number", methods=["GET", "POST"])
@login_required
def number():
    with open("words_number.text", "r") as f:
        problems = f.readlines()
        # print("1個目")
        # print(problems)
        # 改行なくした
        problems = [x.strip() for x in problems]
        # print("2個目")
        # print(problem)
        wordlist = []
        for index, p in enumerate(problems):
            # print(p)
            x = p.split(",")
            # print(x)
            korean = x[1]
            japanese = x[2]
            kanji = x[0]
            wordlist.append(kanji)
            wordlist.append(korean)
            wordlist.append(japanese)
            # print("======第{}問目======".format(index + 1))
            # print(korean)
            # 2秒待つ
            # time.sleep(1)
            # print(japanese)
            # time.sleep(0.5)
            # print(kanji)
        wordlist = zip(*[iter(wordlist)]*3)
        # for word in wordlist:
        #     print(word)
        #     print(word[0])
        #     print(word[1])
        #     print(word[2])
        # print(wordlist)

    return render_template("number.html", wordlist = wordlist)


@app.route("/move", methods=["GET", "POST"])
@login_required
def move():
    with open("words_move.text", "r") as f:
        problems = f.readlines()
        problems = [x.strip() for x in problems]
        wordlist = []
        for index, p in enumerate(problems):
            # print(p)
            x = p.split(",")
            # print(x)
            korean = x[1]
            japanese = x[2]
            kanji = x[0]
            wordlist.append(kanji)
            wordlist.append(korean)
            wordlist.append(japanese)
        wordlist = zip(*[iter(wordlist)]*3)
    return render_template("move.html", wordlist = wordlist)


@app.route("/animal", methods=["GET", "POST"])
@login_required
def animal():
    with open("words_animal.text", "r") as f:
        problems = f.readlines()
        problems = [x.strip() for x in problems]
        wordlist = []
        for index, p in enumerate(problems):
            x = p.split(",")
            korean = x[1]
            japanese = x[2]
            kanji = x[0]
            wordlist.append(kanji)
            wordlist.append(korean)
            wordlist.append(japanese)
        wordlist = zip(*[iter(wordlist)]*3)
    return render_template("animal.html", wordlist = wordlist)


@app.route("/emotion", methods=["GET", "POST"])
@login_required
def emotion():
    with open("words_emotion.text", "r") as f:
        problems = f.readlines()
        problems = [x.strip() for x in problems]
        wordlist = []
        for index, p in enumerate(problems):
            x = p.split(",")
            korean = x[1]
            japanese = x[2]
            kanji = x[0]
            wordlist.append(kanji)
            wordlist.append(korean)
            wordlist.append(japanese)
        wordlist = zip(*[iter(wordlist)]*3)
    return render_template("emotion.html", wordlist = wordlist)


@app.route("/day", methods=["GET", "POST"])
@login_required
def day():
    with open("words_day.text", "r") as f:
        problems = f.readlines()
        problems = [x.strip() for x in problems]
        wordlist = []
        for index, p in enumerate(problems):
            x = p.split(",")
            korean = x[1]
            japanese = x[2]
            kanji = x[0]
            wordlist.append(kanji)
            wordlist.append(korean)
            wordlist.append(japanese)
        wordlist = zip(*[iter(wordlist)]*3)
    return render_template("day.html", wordlist = wordlist)


@app.route("/live", methods=["GET", "POST"])
@login_required
def live():
    with open("words_live.text", "r") as f:
        problems = f.readlines()
        problems = [x.strip() for x in problems]
        wordlist = []
        for index, p in enumerate(problems):
            x = p.split(",")
            korean = x[1]
            japanese = x[2]
            kanji = x[0]
            wordlist.append(kanji)
            wordlist.append(korean)
            wordlist.append(japanese)
        wordlist = zip(*[iter(wordlist)]*3)
    return render_template("live.html", wordlist = wordlist)


@app.route("/test", methods=["GET", "POST"])
@login_required
def test():
    return render_template("test.html")


@app.route("/move_test", methods=["GET", "POST"])
@login_required
def move_test():
    with open("words_move.text", "r") as f:
        problems = f.readlines()
        problems = [x.strip() for x in problems]
        wordlist = []
        for index, p in enumerate(problems):
            x = p.split(",")
            korean = x[1]
            japanese = x[2]
            kanji = x[0]
            wordlist.append(kanji)
            wordlist.append(korean)
            wordlist.append(japanese)
        wordlist = zip(*[iter(wordlist)]*3)
    return render_template("move_test.html", wordlist = wordlist)


@app.route("/number_test", methods=["GET", "POST"])
@login_required
def number_test():
    with open("words_number.text", "r") as f:
        problems = f.readlines()
        problems = [x.strip() for x in problems]
        wordlist = []
        for index, p in enumerate(problems):
            # print(p)
            x = p.split(",")
            # print(x)
            korean = x[1]
            japanese = x[2]
            kanji = x[0]
            wordlist.append(kanji)
            wordlist.append(korean)
            wordlist.append(japanese)
        wordlist = zip(*[iter(wordlist)]*3)
    return render_template("number_test.html", wordlist = wordlist)


@app.route("/animal_test", methods=["GET", "POST"])
@login_required
def animal_test():
    with open("words_animal.text", "r") as f:
        problems = f.readlines()
        problems = [x.strip() for x in problems]
        wordlist = []
        for index, p in enumerate(problems):
            x = p.split(",")
            korean = x[1]
            japanese = x[2]
            kanji = x[0]
            wordlist.append(kanji)
            wordlist.append(korean)
            wordlist.append(japanese)
        wordlist = zip(*[iter(wordlist)]*3)
    return render_template("animal_test.html", wordlist = wordlist)


@app.route("/emotion_test", methods=["GET", "POST"])
@login_required
def emotion_test():
    with open("words_emotion.text", "r") as f:
        problems = f.readlines()
        problems = [x.strip() for x in problems]
        wordlist = []
        for index, p in enumerate(problems):
            x = p.split(",")
            korean = x[1]
            japanese = x[2]
            kanji = x[0]
            wordlist.append(kanji)
            wordlist.append(korean)
            wordlist.append(japanese)
        wordlist = zip(*[iter(wordlist)]*3)
    return render_template("emotion_test.html", wordlist = wordlist)


@app.route("/day_test", methods=["GET", "POST"])
@login_required
def day_test():
    with open("words_day.text", "r") as f:
        problems = f.readlines()
        problems = [x.strip() for x in problems]
        wordlist = []
        for index, p in enumerate(problems):
            x = p.split(",")
            korean = x[1]
            japanese = x[2]
            kanji = x[0]
            wordlist.append(kanji)
            wordlist.append(korean)
            wordlist.append(japanese)
        wordlist = zip(*[iter(wordlist)]*3)
    return render_template("day_test.html", wordlist = wordlist)


@app.route("/live_test", methods=["GET", "POST"])
@login_required
def live_test():
    with open("words_live.text", "r") as f:
        problems = f.readlines()
        problems = [x.strip() for x in problems]
        wordlist = []
        for index, p in enumerate(problems):
            x = p.split(",")
            korean = x[1]
            japanese = x[2]
            kanji = x[0]
            wordlist.append(kanji)
            wordlist.append(korean)
            wordlist.append(japanese)
        wordlist = zip(*[iter(wordlist)]*3)
    return render_template("live_test.html", wordlist = wordlist)


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    if request.method == "POST":
        username = request.form.get("username")
        if not username:
            return apology("Missing username")
        elif not request.form.get("password"):
            return apology("Missing password")
        elif not request.form.get("confirmation"):
            return apology("Missing confirmation")
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("Passwords is not match")
        hash = generate_password_hash(request.form.get("password"))
        try:
            db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, hash)
            return redirect("/")
        except:
            return apology("You cannot use this username")
    else:
        return render_template("register.html")


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
