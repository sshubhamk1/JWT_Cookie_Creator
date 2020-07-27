from webApp import app
from flask import render_template, url_for, request
app.secret_key = "akdsjflaijifiawelfjaiowjeifaliweiflajwiefjiaweifaiwef" # this is a random string

@app.route("/")
def welcome():
    return "<b>Web App created</b>"