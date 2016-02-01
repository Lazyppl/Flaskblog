from flask import render_template, redirect, request, url_for, flash
from flask.ext.login import login_user, login_required
from . import auth
from app.models import User
from .forms import LoginForm, RegistrationForm
from app import db

@auth.route('/')
@auth.route('/blog')
def blog():
    return render_template('blog.html')

@auth.route('/admin', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('auth.blog'))
        flash('invalid username or password')
    return render_template('auth/login.html', form = form)
    
@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Thanks for registering, you can now login to the blog')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)

@auth.route('/profile')
def profile():
    return render_template('profile.html')
    
@auth.route('/contact')
def contact():
    return render_template('contact.html')

