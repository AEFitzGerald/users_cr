from flask import Flask, render_template, redirect, session, request
from customers import Customers

app = Flask(__name__)
app.secret_key = "new store"


@app.route('/')
def index():
    #landpage click to add customer or view account database
    return render_template('index.html')


@app.route('/form')
def form():
    #form to enter new customer
    return render_template('create.html')


@app.route('/customers/create', methods = ['POST'] )
def create_customers():
    #data posted to database and new customer account created
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email_address': request.form['email_address']   
    }
    Customers.new_customer(data)
    #redirect display of customer database
    return redirect('/display')


@app.route('/display')
def display_customers():
    customers = Customers.display_list()
    return render_template('readall.html', customers = customers)
    
    
if __name__=="__main__":
    app.run(debug = True)

