from flask import Flask, render_template, request, redirect, flash, make_response, session
app=Flask(__name__)
app.secret_key="hani"
@app.route('/',methods=['POST','GET'])
def count():
    if 'counter' in session:
        session['counter'] = session.get('counter')+1
    else:
        session['counter']=1
    c = str(session.get('counter'))
    return render_template ('index.html', c=c)

@app.route('/clear',methods=['POST','GET'])
def clear():
    session.clear()
    session['counter']=0
    c = str(session.get('counter')) 
    return render_template('index.html', c=c)

@app.route('/increase',methods=['POST','GET'])
def increase():
    if 'counter' in session:
        session['counter'] = session.get('counter')+2

    c = str(session.get('counter'))
    return render_template('index.html', c=c)

@app.route('/inacc',methods=['POST','GET'])
def inacc():
    y=request.form['var']
    z=int(y)
    if 'counter' in session:
        session['counter'] = session.get('counter')+z

    c = str(session.get('counter'))
    return render_template('index.html', c=c, y=y)
    
app.run(debug=True)