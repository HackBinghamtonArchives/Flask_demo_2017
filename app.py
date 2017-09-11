from flask import Flask, render_template, request
from models import *
from forms import MemberCreateForm
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
csrf = CSRFProtect(app)
app.secret_key = "hnjvshfipu89hiuoabhakldshvjklahrguihuilhu"

def create_tables():
    db.connect()
    db.create_tables([Language, Member, Workshop])

@app.route("/")
def index():
    return "Hi Hackbu! <a href='/create'>Create member</a>"

@app.route("/create", methods=["GET", "POST"])
def create_member():
    if request.method == "POST":
        return "Handle data here!"
    form = MemberCreateForm()
    return render_template("create_member.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
