from flask import Flask
from kik_app.main.controllers import main

app = Flask(__name__)
app.register_blueprint(main)
