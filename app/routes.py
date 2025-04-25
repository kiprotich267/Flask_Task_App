from flask import render_template,flash, request
from app import app, db
from app.models import User
from app.models import Task
from app.forms import TaskForm, UserForm, LoginForm
from flask import redirect, url_for
from flask_login import login_user, login_required,  logout_user, current_user


@app.route('/')

def home():
    users = User.query.all()
    user_count = User.query.count()
  
    return render_template('index.html', user_count=user_count,  users=users, title='Home')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = UserForm()
    if form.validate_on_submit():
        new_user = User(
            username=form.username.data, 
            first_name=form.first_name.data,
            last_name=form.last_name.data, 
            password=form.password.data)       
        
        db.session.add(new_user)
        db.session.commit()
        flash(f'registration for {new_user.first_name} successfully!', 'success')
        return redirect(url_for('register'))
    print(form.errors)
    return render_template('register.html',title='Register', user_form=form)
    



@app.route('/tasks', methods=['GET', 'POST'])
@login_required
def tasks():
    tasks = Task.query.all()
    task_count = Task.query.count()
    form = TaskForm()
    if form.validate_on_submit():
        new_task = Task(
            title=form.title.data,
            description=form.description.data,
            completed=form.completed.data,
            user_id=current_user.id
        )
        db.session.add(new_task)
        db.session.commit()
        flash(f'Task {new_task.title} added successfully!', 'success')
        return redirect(url_for('tasks'))
    tasks = Task.query.filter_by(user_id=current_user.id).all()
  
    return render_template('tasks.html', title='Tasks', tasks=tasks, task_count=task_count, form=form)

@app.route('/toggle_task/<int:task_id>' , methods=['POST'])
def toggle_task(task_id):
    task = Task.query.get_or_404(task_id)
    task.completed = not task.completed
    db.session.commit()
    flash(f'Task {task.title} updated successfully!', 'success')
    return redirect(url_for('tasks'))




@app.route('/delete_user/<int:user_id>', methods=['POST'])
@login_required
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash(f'User {user.username} deleted successfully!', 'success')
    return redirect(url_for('home'))

@app.route('/delete_task/<int:task_id>', methods=['POST'])
@login_required
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    flash(f'Task {task.title} deleted successfully!', 'success')
    return redirect(url_for('tasks'))

@app.route('/edit_task/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    form = TaskForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            task.title = form.title.data
            task.description = form.description.data
            task.completed = form.completed.data
            db.session.commit()
            flash(f'Task {task.title} updated successfully!', 'success')
            return redirect(url_for('tasks'))
        
    elif request.method == 'GET':
            form.title.data = task.title
            form.description.data = task.description
            form.completed.data = task.completed
        
            tasks = Task.query.all()
        
        
    return render_template('tasks.html', title='Edit Tasks', tasks=tasks, form=form, edit_mode=True)


@app.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            flash(f'Welcome back, {user.first_name}!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password', 'danger')

    return render_template('login.html', title='Login', login_form=form)

@app.route('/logout')
def logout():
    logout_user()
    flash('logged out successfully!', 'success')
    return redirect(url_for('home'))