from flask import Flask, render_template,request
app=Flask(__name__)

@app.route("/") #decorator function
def root():
    return render_template("results.html")

@app.route("/submit",methods=["POST"])
def calculate():
    
    w1=float(request.form['w1'])
    m1=float(request.form['m1'])
    w2=float(request.form['w2'])
    m2=float(request.form['m2'])

    score = (m1*w1+m2*w2)/100
    return render_template("results.html" , m1=m1,m2=m2,w1=w1,w2=w2, score= score)

app.run(debug=True)