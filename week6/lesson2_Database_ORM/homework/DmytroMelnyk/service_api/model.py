from week6.lesson2_Database_ORM.homework.DmytroMelnyk.service_api.app_database import db


class  (db.Model):
    __tablename__ = "user_table"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(80))
    userage = db.Column(db.Integer)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String)

    def __init__(self, id, username, age, email, password):
        self.id = id
        self.username = username
        self.age = age
        self.email = email
        self.password = password

    def __repr__(self):
        return f'<User {self.username}>'


class CarTable(db.Model):
    __tablename__ = "cars_table"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    model = db.Column(db.String(80))
    mark = db.Column(db.String(80))
    horsepower = db.Column(db.Integer)
    year = db.Column(db.String(10))
    origin = db.Column(db.String(80))

    def __init__(self, id, model, mark, horsepoewer, year, origin):
        self.id = id
        self.model = model
        self.mark = mark
        self.horsepoewer = horsepoewer
        self.year = year
        self.origin = origin
