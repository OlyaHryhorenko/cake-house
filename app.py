from flask import Flask, flash, redirect, render_template, \
     request, url_for
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/tutorial'
app.secret_key = 'some_secret'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    password = db.Column(db.String(128))


class Cake(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.String(100))
    photo_path = db.Column(db.String(255))

    def __init__(self, title=None, description=None, photo_path=None):
        self.title = title
        self.description = description
        self.photo_path = photo_path



@app.route("/")
def main():
    return render_template("index.html")


@app.route("/admin")
def admin():
    return render_template("admin.html")


@app.route("/add-cake", methods=['POST'])
def add_cake():
    title = request.form.get('title')
    description = request.form.get('description')
    cake = Cake(title, description, 'sdsdsd')
    db.session.add(cake)
    db.session.commit()
    flash('Cake added')
    return redirect(url_for('admin'))



if __name__ == "__main__":
    app.run()