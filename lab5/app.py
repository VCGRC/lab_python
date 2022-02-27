import requests
from flask import Flask, render_template, request, redirect
import pymongo

app = Flask(__name__)
cluster = pymongo.MongoClient('localhost')
user_collection = cluster.labs.users

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        data = request.form.to_dict()

        if data['username'] == '' or data['password'] =='':
            return "Опа пустые данные"

        user_info = user_collection.find_one({'username':data['username'], "password":data['password']})
        
        if user_info is None:
            return render_template('profile.html')
        
        return render_template('profile.html', full_name = user_info['full_name'])

@app.route('/registration', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('registration.html')
    elif request.method == 'POST':
        data = request.form.to_dict()

        if data['username'] == '' or data['password'] =='' or data['full_name'] =='':
            return "Опа пустые данные"

        user_info = user_collection.find_one({'username':data['username']})
        
        if user_info is not None:
            return "Вы уже зарегистрированны"
        else:
            user_collection.insert_one(data)
            # return "Вы уже зарегистрированы"
            return redirect('/login')
        

app.run()