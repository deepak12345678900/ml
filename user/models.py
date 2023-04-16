from flask import Flask,jsonify,request
from passlib.hash import pbkdf2_sha256
from app import app
import uuid
class User:
    def signup(self):
        user={
            "id":uuid.uuid4().hex,
            "name":request.form.get('name'),
            "email":request.form.get('email'),
            "password":request.form.get('password')
        }
        user['password']=pbkdf2_sha256.encrypt(user['password'])
        return jsonify(user),200