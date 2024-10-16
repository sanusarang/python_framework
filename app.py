from flask import Flask, render_template
app=Flask(__name__)

@app.route("/index",methods=['GET'])
def hello_world():
    return render_template("index.html")

@app.route("/product",methods=['GET'])
def product():
    return render_template("product.html")

if __name__==("__main__"):
    app.run(debug=True)
