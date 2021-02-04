from flask import Flask, render_template, request
import pymongo
import os
from flask_pymongo import PyMongo
app=Flask(__name__)
#we are searching for a dictionary called os.environ, "MONGO_URI" is a key that might exist in this dictionary and its value is supposed to be the connection string
#"MONGO_URI" exists on heroku because we have added it manually before deploying the app, it does not exist locally because we haven't added it
#if we are searching for the dictionary and None is printed (it is local), connectionstring.txt (where the connection string is stored) must be opened and read
#

var=os.environ.get("MONGO_URI")
print(os.environ.get("MONGO_URI"))
if var==None:
    file=open("connectionstring.txt",'r')
    connectionstring=file.read().strip()
    app.config["MONGO_URI"]=connectionstring
else:
    app.config["MONGO_URI"]=os.environ.get("MONGO_URI")
mongo=PyMongo(app)

@app.route("/")
def index():
    return render_template("index.html")
    


@app.route("/insert_notes",methods=["GET","POST"])
def insertnotes():
    if request.method=="GET":
        return render_template("insertnotes.html")
    else:
        name=request.form["namebox"]
        note=request.form["notebox"]
        notes={"name":name,"note":note}
        mongo.db.notes.insert_one(notes)
        return("Note created")







@app.route("/show_notes")
def shownotes():
    allnotes={}
    notes=mongo.db.notes.find()
    for var in notes:
        allnotes[var["name"]]=var["note"]
    return render_template("show_notes.html",allnotes=allnotes)
       





#adding comment







if __name__=="__main__":
    app.run()