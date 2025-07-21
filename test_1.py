from flask import Flask,request

test_1 = Flask(__name__)
print(__name__)

@test_1.route('/')
def Aakash_AJ():
    return "<h1>Hello, Aakash AJ! - this is your first Flask test</h1>"

@test_1.route('/add')
def Add1():
    a = request.args.get('a')
    b = request.args.get('b')
    return f"<h1>Addition of {a} and {b} is {a + b}</h1>"


@test_1.route('/add2')
def Add2():
    a = request.args.get('a')
    b = request.args.get('b')
    return "<h1>Addition of {}</h1>".format(int(a) + int(b))



if __name__ == '__main__':
    test_1.run(debug=True,host="0.0.0.0", port=5000)
