from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = ''
    expression = ''

    if request.method == 'POST':
        expression = request.form.get('expression', '')
        
        # Allow only digits, operators, decimal, and parentheses
        if re.match(r'^[0-9+\-*/(). ]+$', expression):
            try:
                result = str(eval(expression))
            except Exception:
                result = 'Error'
        else:
            result = 'Invalid input'
    
    return render_template('index.html', result=result, expression=expression)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
