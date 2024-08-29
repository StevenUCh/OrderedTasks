from flask import Blueprint, render_template, redirect, url_for, request
from app import db
from app.models import Task, User
from app.forms import TaskForm
from flask_login import login_user, current_user, logout_user, login_required
from app.forms import RegistrationForm, LoginForm, TaskForm

bp = Blueprint('main', __name__)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            return redirect(url_for('main.index'))
    return render_template('login.html', form=form)

@bp.route('/')
@login_required
def index():
    tasks = Task.query.filter_by(owner=current_user).all()
    return render_template('index.html', tasks=tasks)

@bp.route('/add_task', methods=['POST'])
@login_required
def add_task():
    form = TaskForm()
    if form.validate_on_submit():
        task = Task(title=form.title.data, due_date=form.due_date.data, owner=current_user)
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('main.index'))
    return redirect(url_for('main.new_task'))

@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    print("=== ")
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('main.index'))
    return render_template('register.html', form=form)

@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@bp.route('/task/new', methods=['GET', 'POST'])
@login_required
def new_task():
    form = TaskForm()
    if form.validate_on_submit():
        task = Task(
            title=form.title.data,
            description=form.description.data,
            due_date=form.due_date.data,
            owner=current_user 
        )
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('task_form.html', form=form)
