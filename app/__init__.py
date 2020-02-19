from flask import Flask
from flask_mail import Mail

app = Flask(__name__)

app.config["SECRET_KEY"] = "9rj)(wBEGhbP_<Ka"
app.config["MAIL_SERVER"] = "smtp.mailtrap.io"
app.config["MAIL_PORT"] = "465"
app.config["MAIL_USERNAME"] = "3c4cf6a715e870"
app.config["MAIL_PASSWORD"] = "2519a1a4fe3a33"

mail = Mail(app)
from app import views

