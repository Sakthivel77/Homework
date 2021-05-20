import csv
from flask import Flask, render_template, request

with open('exchange_rates.txt') as f:
    reader = csv.reader(f)
    l2 = []
    for line in reader:
        conversion = float(line[4])/float(line[3])
        l2 += [[line[1][1:],line[2][1:],conversion,'..\\static\\flags\\'+line[2][1:]+'.png']]


app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/submit' , methods = ['POST'])
def submit():
    sgd = float(request.form['SGD'])
    
    for line in l2:
        value = line[2]*sgd
        line.append(value)

    print(l2)

    
    return render_template('index2.html', l2 = l2)

app.run(debug=True)