from flask import Flask, render_template, request
import pymongo
app=Flask(__name__)
file=open("connectionstring.txt",'r')
connectionstring=file.read()
print(connectionstring)
print("hello")
# client=pymongo.MongoClient(connectionstring)
# database=client["notemanager"]
# mycollection=database["notes"]



# @app.route("/",methods=["GET","POST"])
# def index():
#     if request.method=="GET":
#         return render_template("index.html")
#     else:
#         name=request.form["namebox"]
#         note=request.form["notebox"]
#         record={"name":name,"note":note}
#         mycollection.insert_one(record)
#         print(name,note)
#         return("information is submitted")












# if __name__=="__main__":
#     app.run(debug=True)