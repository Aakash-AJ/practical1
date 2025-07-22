from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

main = Flask(__name__)


@main.route("/add", methods=["POST", "GET"])
def user_details():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        age = request.form["age"]
        location = request.form["location"]

        return jsonify(
            {
                "message": "User details added successfully!",
                "data": {
                    "username": username,
                    "email": email,
                    "age": age,
                    "location": location,
                },
            }
        )
    return render_template("index.html")


if __name__ == "__main__":
    main.run(host="0.0.0.0")
