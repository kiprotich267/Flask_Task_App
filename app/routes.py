
from flask import render_template
from app import app
from app.models import User

users = ["rop", "kirui", "kipngeno", "dorothy", "enock"]



@app.route('/')
def home():
    users = User.query.all()
    return render_template('index.html', users=users)


