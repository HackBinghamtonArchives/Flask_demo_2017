from flask import Flask, render_template, request, redirect
from models import *
from forms import MemberCreateForm
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
csrf = CSRFProtect(app)
app.secret_key = "hnjvshfipu89hiuoabhakldshvjklahrguihuilhu"

# @app.before_request
# def db_connect():
#     #db is pulled from models in * import
#     db.get_conn() #connection
#
# @app.teardown_request
# def db_disconnect():
#     if not db.is_closed():
#         db.close()

def create_tables():
    try:
        db.create_tables([Language, Member, Workshop], safe=True)
    except OperationalError as e:
        print("Tables already exist")


@app.route("/")
def index():
    return "Hi Hackbu! <a href='/create'>Create member</a>"

@app.route("/create", methods=["GET", "POST"])
def create_member():
    if request.method == "POST":
        print(request.form)
        try:
            with db.transaction():
                member = Member.create(name=request.form["name"],
                                       checked_in=True if request.form["checked_in"]=="y" else False
                                        )
                return redirect("/members")
        except Exception as e:
            print(e)

    form = MemberCreateForm()
    return render_template("create_member.html", form=form)

@app.route("/members")
def list_members():
    members = Member.select()
    return render_template("list_members.html", members=members)

if __name__ == "__main__":
    # if you create new tables, make sure to create them from the command line
    # from app import *
    create_tables()
    app.run(debug=True)
