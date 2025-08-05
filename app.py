from flask import Flask, render_template, request

app = Flask(__name__)
cost = {1:80, 2:100}
@app.route('/')
def home():
    return render_template('homepage.html')
@app.route('/pg1')
def pg1():
    return render_template('pg1.html')
@app.route('/b1')
def b1():
    return render_template('b1.html')
@app.route('/b2')
def b2():
    return render_template('b2.html')
if __name__ == '__main__':
    app.run(debug=True)
