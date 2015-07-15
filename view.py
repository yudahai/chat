#coding:utf-8
from flask import Flask, session, redirect, url_for, request, flash, render_template, Markup, g, jsonify, \
    stream_with_context, Response, abort
from model import *
from wtforms import Form, BooleanField, TextField, PasswordField, validators, StringField, SelectField, RadioField


app = Flask(__name__)
app.secret_key = 'diiiffidifidfid-9933jjjj'


@app.teardown_request
def handle_teardown_request(exception):
    db_session.remove()


@app.route('/')
def index():
    return render_template('index.html')