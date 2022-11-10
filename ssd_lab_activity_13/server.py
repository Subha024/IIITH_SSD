from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import (LoginManager, login_manager,
    login_user, logout_user, login_required, UserMixin)
import json

# configuring the application
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///user.db"

db = SQLAlchemy(app)

class User(db.Model):
    bookingId = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), nullable = False)
    email = db.Column(db.String(80), nullable = False)
    bookingStatus = db.Column(db.String(80), nullable = False)
    bookingType = db.Column(db.String(80), nullable = False)
    bookingDateTime = db.Column(db.DateTime(80), nullable = False)
    bookedSeatsCount = db.Column(db.String(80), nullable = False)
    seats = db.Column(db.String(80), nullable = False)
    
with app.app_context():
    db.create_all()

@app.route("/seats/booking/<bookingId>", methods = ["GET"])
def  fetch_booked_ticket(bookingId):
    return jsonify({
        "bookingId": bookingId
    })
        

if __name__ == "__main__":
    app.run(host = "127.0.0.1", port = "5000", debug = True)

