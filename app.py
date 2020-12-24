from flask import Flask, render_template, request
app=Flask(__name__)



@app.route("/",methods=["GET","POST"])
def index():
    if request.method=="GET":
        return render_template("index.html")
    else:
        name=request.form["namebox"]
        note=request.form["notebox"]
        print(name,note)
        return("information is submitted")












if __name__=="__main__":
    app.run(debug=True)