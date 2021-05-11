from flask import Flask, render_template
app = Flask(__name__) 

@app.route('/')          
def hello_world():
     return 'Hello World!'


@app.route('/success')
def success():
    return "success"


@app.route('/dojo')          
def hello_world1():
    return 'Dojo!'

@app.route('/say/<name>')          
def say(name):
    return f"hi {name}"

#@app.route('/<word>/<num>')
#def index(word,num):
    
#    return word * int(num) 

@app.errorhandler(404)
def page_not_found(e):
    return ('sorry try it again')







if __name__=="__main__":   
    app.run(debug=True) 