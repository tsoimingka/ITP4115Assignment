from datetime import datetime
from flask import render_template, flash, redirect, request, url_for
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, SignupForm
from app.models import User, Programme_Language, Subject

@app.before_request
def brfore_request():
    if current_user.is_authenticated:
        print(current_user.username)
        current_user.last_seen = datetime.utcnow()
        db.session.commit()
    pl = Programme_Language
    s = Subject
    
        
#首頁
@app.route('/', methods=['GET', 'POST'])
def index():
    form = SignupForm()
    if form.validate_on_submit():
        if User.query.filter_by(username=form.username.data).first():
            flash("username already exists")
        else:
            user = User(form.username.data, form.password.data)
            db.session.add(user)
            db.session.commit()
            login_user(user)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('learn')
            return redirect(next_page)
    return render_template('index.html', title='Learn to Code - for Free', form=form)
    
#個人空間
@app.route('/learn')
def learn():
    return render_template('profiles.html')

#註冊
@app.route('/register')
def register():
    return render_template('register.html')

#登入
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user is None:
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user)
        next_page = url_for('learn')
        return redirect(next_page)
    return render_template('login.html', title="Log in", form=form)

@app.route('/logout')
def logout():
    print(current_user)
    logout_user()
    return redirect(url_for('index'))

@app.route('/catalog')
def catalog():
    render_template('base_2.html', pl=Programme_Language, s=Subject)
    return render_template('catalog.html', title='Catalog Home', pl=Programme_Language, s=Subject)


@app.route('/resources/cheatsheets')
def cheatsheets():
    return render_template('cheatsheets.html')
    
@app.route('/catalog/<name>')
def language(name):
    data = Programme_Language.query.filter_by(name=name).first()
    return render_template('language.html', title=name + "Courses & Tutorials", data=data, pl=Programme_Language, s=Subject)
    
@app.route('/catalog/Subject/<name>')
def subjects(name):
    return render_template('subject.html', title=name + "Courses & Tutorials", data=s_data, pl=Programme_Language, s=Subject)