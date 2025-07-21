from flask import Flask, request, render_template, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# ✅ MongoDB Connection
client = MongoClient("mongodb://localhost:27017/")  # Or use your Atlas URI
db = client['flask_db']          # Database name
calc_collection = db['calculations']  # Collection name

# ✅ New user_details collection
user_collection = db['user_details']

@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        data = request.form
        name = data.get('name')
        email = data.get('email')
        age = data.get('age')
        dob = data.get('dob')
        if not all([name, email, age, dob]):
            return "<h1>Missing user details</h1>", 400
        user_collection.insert_one({
            "name": name,
            "email": email,
            "age": age,
            "dob": dob
        })
        return "<h1>User added successfully!</h1>", 201
    else:
        return render_template('home.html')

@app.route('/list', methods=['GET'])
def list_users_and_calculations():
    users = list(user_collection.find())
    calculations = list(calc_collection.find({}, {'_id': 0}))
    return render_template('list.html', users=users, calculations=calculations)

@app.route('/api', methods=['GET'])
def api():
    data = {
        "message": "Hello, World!",
        "status": "success"
    }
    return jsonify(data)

@app.route('/calculator', methods=['GET', 'POST'])
def Calculator():
    a = request.args.get('a')
    b = request.args.get('b')
    operation = request.args.get('operation')
    print(a, b, operation)

    if not all([a, b, operation]):
        return "<h1>Missing input</h1>"

    try:
        a = int(a)
        b = int(b)
    except ValueError:
        return "<h1>Inputs must be numbers</h1>"

    if operation == 'add':
        result = a + b
    elif operation == 'subtract':
        result = a - b
    elif operation == 'multiply':
        result = a * b
    elif operation == 'divide':
        result = a / b if b != 0 else 'Infinity'
    else:
        return "<h1>Invalid operation</h1>"

    # ✅ Save to MongoDB
    calc_collection.insert_one({
        "a": a,
        "b": b,
        "operation": operation,
        "result": result
    })

    return render_template('index.html', result=result, a=a, b=b, operation=operation)

@app.route('/')
def home():
    return render_template('home.html', name="Aakash")


@app.route('/calculations', methods=['GET'])
def calculations():
    calculations = list(calc_collection.find())
    return render_template('calculations.html', calculations=calculations)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
