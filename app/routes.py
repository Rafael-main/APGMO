import string
import secrets
from secrets import choice
from passlib.context import CryptContext
from flask import Flask, render_template, Blueprint, redirect, url_for, session, flash, request, jsonify, make_response
from app import app

@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html", title="APGMO")

@app.route('/profile')
def profile():
    return render_template("profile.html", title="APGMO")

@app.route('/lets_go', methods=['POST'])
def lets_go():
    req = request.get_json()

    res = make_response(jsonify({"message": "OK"}), 200)

    return res



@app.route('/generate', methods = ['POST'])
def gen_pass():
    if request.method:
        req = request.get_json()

        pass_len = req['pass_length']
        pass_abc_caps = req['alpha_caps']
        pass_abc_noncaps = req['alpha_noncaps']
        pass_spec_char = req['spec_char']
        pass_digits = req['pass_length']


        spec_char = """!#$%&*+-=?@^_{|}~"'"""

        if pass_len and pass_abc_caps and pass_abc_noncaps and pass_spec_char and pass_digits:
           strings = string.ascii_letters + string.digits + string.punctuation
        if pass_len and pass_abc_caps and pass_abc_noncaps and pass_spec_char:
            strings = string.ascii_letters + string.punctuation
        elif pass_len and pass_abc_noncaps and pass_spec_char and pass_digits:
            strings = string.ascii_lowercase + string.punctuation + string.digits
        elif pass_len and pass_abc_noncaps and pass_spec_char and pass_digits:
            strings = string.ascii_uppercase + string.punctuation + string.digits

        while True:
            password = ''.join(secrets.choice(strings) for i in range(pass_len))
            if (any(c.islower() for c in password)
                    and any(c.isalpha() for c in password)
                    and sum(c.isdigit() for c in password)):
                break
        
        return make_response(jsonify({"password": password}), 200)
