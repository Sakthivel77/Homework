from flask import Flask, render_template,request
app=Flask(__name__)

@app.route("/") #decorator function
def root():
    return render_template("form1.html")

@app.route("/submit",methods=["POST"])
def calculate():
    output = f'Hello {request.form["Name"]}, your email is {request.form["Email"]}'
    return output   

app.run(debug=True)