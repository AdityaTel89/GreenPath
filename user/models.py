from flask import Flask, jsonify

class User:

    def signup(self):

        user={
            "name":request.form.get('username'),
            "email":request.form.get('email'),
            "password":request.form.get('password')
        }

        return jsonify(user), 200