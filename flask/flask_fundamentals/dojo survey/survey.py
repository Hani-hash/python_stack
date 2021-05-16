from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/result', methods=['post'])
def result():
    name=request.form['name']
    location=request.form['location']
    lang=request.form['lang']
    comment=request.form['comment']
    checkbox=request.form['checkbox']
    radio=request.form['radio']

    return render_template("res.html", name=name, location=location, lang=lang, comment=comment, checkbox=checkbox, radio=radio)

app.run(debug=True)
