from flask import Flask, render_template,request,redirect
path = 'C:\\Users\\65820\\Desktop\\Computing HW\\Web\\Exercise 12\\ProductsApp\\static\\images\\'
app=Flask(__name__)

@app.route("/AddProduct",methods=["POST"])
def random():
        return render_template('product_frm.html')

@app.route('/add' ,methods=['POST'])
def add_product():

    image_file = request.files["image"]
    image_file_name=image_file.filename
    if image_file_name != '':
        image_file.save(path+image_file_name)
        
        with open('ProductsApp\static\products.txt' , 'a') as f:
            string = '\n'
            for key in request.form:
                string+= request.form[key] + ','
            string+= image_file_name
            f.write(string)
        #open products.txt
        #pass
        #upload image file if the key "image" is in the request.files dictionary
        #write new product data to products.txt
        #pass
        #pass
    return redirect("/")

@app.route("/") #decorator function
def root():
    with open('ProductsApp\static\products.txt') as f:
        x = f.read().splitlines()
        products= []
        for line in x:
            info = line.split(',')
            info[3] = '../static/images/'+info[3]
            if '$' not in info[2]:
                info[2] = '$' + info[2]
            products.append(info)
    return render_template("products.html" , products = products)


app.run(debug=True)
