from flask import Flask, jsonify, request
from db_module import *

app = Flask(__name__)

@app.route('/get_all_users')
def get_users():
    return jsonify(getUsers())


#@app.route('/add_user', methods = ['POST'])

@app.route('/add_user', methods = ['POST'])
def add_user():
    data = request.get_json()
    id = data['id']
    password = data['password']

    if id == '' or password == '':
        return jsonify({'message' : 'Missing one or more inputs'})
    insertUser(id, password)
    return jsonify({'message': 'User added successfully'})


@app.route('/update_user', methods = ['POST'])
def update_user():
    data = request.get_json()
    id = data['id']
    password = data['password']

    if id == '' or password == '':
        return jsonify({'message' : 'Missing one or more inputs'})
    updateUser(id, password)
    return jsonify({'message': 'User updated successfully'})


@app.route('/delete_user', methods = ['POST'])
def delete_user():
    data = request.get_json()
    id = data['id']

    if id == '':
        return jsonify({'message' : 'Missing one or more inputs'})
    deleteUser(id)
    return jsonify({'message': 'User deleted successfully'})

@app.route('/delete_user_get/<string:id>')
def delete_user_temp(id):
    if id == '':
        return jsonify({'message' : 'Missing one or more inputs'})
    deleteUser(id)
    return jsonify({'message': 'User deleted successfully'})


@app.route('/authenicate_user', methods = ['POST'])
def authenicateUser():
    data = request.get_json()
    id = data['id']
    password = data['password']

    if id == '' or password == '':
        return jsonify({'message' : 'Missing one or more inputs'})
    result = login(id, password)

    if result:
        message = 'User authentication successful'
    else:
        message = 'User authenticatio failed'
    return jsonify({'message': message})

app.run(port = 5000)


