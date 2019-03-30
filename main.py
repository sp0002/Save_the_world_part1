from flask import Flask, redirect, render_template

app = Flask(__name__)

url_for('static', filename = 'index.css')
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/explanation)
def explanation():
    return render_template("index2.html")
if __name__=="__main__":
    app.run(debug=True)
           
