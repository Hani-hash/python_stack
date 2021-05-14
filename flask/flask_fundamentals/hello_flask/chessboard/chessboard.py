from flask import Flask, render_template

app = Flask(__name__)
    
@app.route("/")
@app.route("/<int:rows>")
@app.route("/<int:rows>/<int:columns>")
@app.route("/<int:rows>/<int:columns>/<color1>/<color2>")
def root(rows=8, columns=8,color1= "black",color2= "white"):
    return render_template("chess.html", rows=rows, columns=columns,color1=color1,color2=color2)


if __name__ == "__main__":
    app.run(debug=True)