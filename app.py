from flask import Flask, render_template, request
import pymongo
app=Flask(__name__)
file=open("connectionstring.txt",'r')
connectionstring=file.read().strip()
client=pymongo.MongoClient(connectionstring)   #connecting to mongo db atlas cluster
database=client["notemanager"]   #notemanager is the database and we are connecting to it
mycollection=database["notes"]  #notes is a collection and we are connecting to it



@app.route("/insert_notes",methods=["GET","POST"])
def insertnotes():
    if request.method=="GET":
        return render_template("index.html")
    else:
        name=request.form["namebox"]
        note=request.form["notebox"]
        notes={"name":name,"note":note}
        mycollection.insert_one(notes)
        return("Note created")







@app.route("/show_notes")
def shownotes():
    allnotes={}
    notes=mycollection.find()
    for var in notes:
        allnotes[var["name"]]=var["note"]
    return render_template("show_notes.html",allnotes=allnotes)
       













if __name__=="__main__":
    app.run()