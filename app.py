from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    age = request.form.get('age')
    return redirect(url_for('anketa', name=name, age=age))

@app.route('/anketa')
def anketa():
    name = request.args.get('name')
    age = request.args.get('age')
    return render_template('anketa.html', name=name, age=age)

if __name__ == '__main__':
    app.run(debug=True)