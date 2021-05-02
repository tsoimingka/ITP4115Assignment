from datetime import datetime
from hashlib import md5
from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

User_Courses = db.Table('user_course',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('course_id', db.Integer, db.ForeignKey('course.id')),
    db.Column('status', db.String(10))
)

class User(UserMixin, db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), index=True, unique=True, nullable=True)
    password = db.Column(db.String(128), nullable=True)
    name = db.Column(db.String(128))
    email = db.Column(db.String(128), nullable=True)
    picture = db.Column(db.LargeBinary(65536), nullable=True)
    location = db.Column(db.String(200), nullable=True)
    website = db.Column(db.String(200), nullable=True)
    github = db.Column(db.String(200), nullable=True)
    twitter = db.Column(db.String(200), nullable=True)
    LinkedIn = db.Column(db.String(200), nullable=True)

    def __init__(self, username, password, name=None):
        self.username = username
        self.password = password
        if name is None:
            name = username
        self.name = name

    def __repr__(self):
        return '<User {}>'.format(self.name)

    def set_password(self, password):
        self.password_hash = generate_password_hash(self, password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class Programme_Language(db.Model):
    __tablename__ = "programme_language"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)
    order_id = db.Column(db.Integer, unique=True)
    description = db.Column(db.String(500))
    
    def __init__(self, name, order_id, description):
        self.name = name
        self.order_id = order_id
        self.description = description
    
class Subject(db.Model):
    __tablename__ = "subject"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)
    order_id = db.Column(db.Integer, unique=True)
    description = db.Column(db.String(300))

    def __init__(self, name, order_id, description):
        self.name = name
        self.order_id = order_id
        self.description = description

class Course_Type(db.Model):
    __tablename__ = "course_type"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)
    
    def __init__(self, name):
        self.name = name

class Course_Difficulty(db.Model):
    __tablename__ = "course_difficulty"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)
    
    def __init__(self, name):
        self.name = name

class Course(db.Model):
    __tablename__ = "course"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)
    type = db.Column(db.Integer, db.ForeignKey('course_type.id'))
    difficulty = db.Column(db.Integer, db.ForeignKey('course_difficulty.id'))
    join = db.Column(db.Integer)
    complete_time = db.Column(db.Integer)
    prerequisites = db.Column(db.Integer)
    
    def __init__(self, name, type=None, difficulty=None,
    earn=None, join=None, complete_time=None, prerequisites=None):
        self.name = name
        self.type = type
        self.join = join
        self.complete_time = complete_time
        self.prerequisites = prerequisites

class Course_Lesson(db.Model):
    __tablename__ = "course_lesson"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)
    order_id = db.Column(db.Integer, unique=True)
    description = db.Column(db.String(300))
    courses_id = db.Column(db.Integer, db.ForeignKey('course.id'))
    
    def __init__(self, name):
        self.name = name