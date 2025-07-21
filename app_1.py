from flask import Flask
app1 = Flask(__name__)

@app1.route('/')
def Aakash_1():
    return "<h1>Aakash Jaiswar is a final-year B.Sc. Statistics student from Mumbai, driven by a strong desire to build a successful career in Data Science. With hands-on experience as a Desktop Support Engineer and practical skills in Python, Excel, Google Sheets, and SQL, he’s actively learning and growing through real-world projects and technical concepts like APIs, MongoDB, and machine learning. He’s a self-aware, hardworking individual who values focus, discipline, and personal development—balancing his studies with gym workouts and a sharp curiosity for boosting intelligence and problem-solving. Aakash is determined to transform his knowledge into action, with clear goals, a resilient mindset, and a never-quit attitude.Aakash Jaiswar is a final-year B.Sc. Statistics student from Mumbai, driven by a strong desire to build a successful career in Data Science. With hands-on experience as a Desktop Support Engineer and practical skills in Python, Excel, Google Sheets, and SQL, he’s actively learning and growing through real-world projects and technical concepts like APIs, MongoDB, and machine learning. He’s a self-aware, hardworking individual who values focus, discipline, and personal development—balancing his studies with gym workouts and a sharp curiosity for boosting intelligence and problem-solving. Aakash is determined to transform his knowledge into action, with clear goals, a resilient mindset, and a never-quit attitude.</h1>"

if __name__ == '__main__':
    app1.run(host="0.0.0.0")