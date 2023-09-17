

# imports
import db
from flask import Flask, redirect, url_for, request
from flask import render_template as show


app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
  show("index.html")
