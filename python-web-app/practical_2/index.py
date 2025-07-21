from flask import Flask, request, jsonify,render_template
from pymongo import MongoClient

app = Flask(__name__)
# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['family']
members_table = db['members']

@app.route('/', methods=['GET'])
def get_data():
    return "<h1>HOME</h1>"

@app.route('/members', methods=['GET', 'POST'])
def members():
    if request.method == 'GET':
        members = list(members_table.find())
        print(members)
        return render_template("index.html", members=members)
    
    elif request.method == 'POST':
        form = request.form
        username = form.get('username')
        email= form.get('email')   

        members_table.insert_one({"username": username, "email": email})
        return jsonify(form), 201

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)