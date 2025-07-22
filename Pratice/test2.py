from flask import Flask, jsonify, request,render_template

app = Flask(__name__)

@app.route('/greet', methods=['GET', 'POST'])
def greet():
    name = request.args.get('name', 'Guest')
    return jsonify({
        'message': f'Hello, {name}!',
        'status': 'success'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
