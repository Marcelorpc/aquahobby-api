from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///aquahobby.db'

db = SQLAlchemy(app)

class Aquarium(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(60), nullable=False)
   volume = db.Column(db.Integer, nullable=False)
   temperature = db.Column(db.Float, nullable=False)
   ph = db.Column(db.Float, nullable=False)


@app.route('/')
def hello_world():
    return 'Hello World'

if __name__ == "__main__":
  app.run(debug=True)