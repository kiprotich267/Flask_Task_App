
from flask import render_template, redirect, url_for
from app import app,db
from app.models import User, Task
from app.forms import TaskForm
from app.forms import UserForm

users = ["rop", "kirui", "kipngeno", "dorothy", "enock"]



@app.route('/')
def home():
    users = User.query.all()


    return render_template('index.html', users=users, title='Home')

@app.route('/tasks', methods=['GET', 'POST'])
def tasks():
    form = TaskForm()
    if form.validate_on_submit(): 
        new_task = Task(
            title=form.title.data,
            description=form.description.data,
            completed=form.completed.data
        )
        db.session.add(new_task)
        db.session.commit()
        tasks = Task.query.all()
        return redirect(url_for('tasks'))
   
    
    return render_template('tasks.html', users=users, title='Tasks', form=form, tasks=tasks )

@app.route('/register', methods=['GET', 'POST'])
def register():
   
    form = UserForm()
    if form.validate_on_submit():
        new_user = User(
            username=form.username.data,
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            password=form.password.data
        )
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('home'))
        
    return render_template('register.html', users=users, title='Register', user_form=form)


