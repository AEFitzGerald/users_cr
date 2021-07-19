# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL

# model the class after the table from our database
class Customers():
    
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email_address = data['email_address']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Use class methods to query the database   
    @classmethod
    def new_customer(cls, data):
        
        query = "INSERT INTO customers (first_name, last_name, email_address) VALUES (%(first_name)s, %(last_name)s, %(email_address)s);"
        # Call the connectToMySQL function with the targeted schema db
        return connectToMySQL('users').query_db(query, data)
        # returns the int of id number 

    @classmethod 
    def get_all_customers(cls):
        
        query = "SELECT * FROM customers;"
        
        results = connectToMySQL('users').query_db(query)
        # Create an empty list to append our instances of customers
        customers = []
        # Iterate over the db results and create instances of customers with cls
        for customer in results:
            customers.append(cls(customer))

        return customers
    
    @classmethod
    def get_customer_by_id(cls,data):
        
        query = "SELECT * FROM customers WHERE id = %(id)s;"
        
        result = connectToMySQL('users').query_db(query,data)
        # customer is equal to the dictionary row pulled from database
        customer = Customers(result[0])

        return customer

    @classmethod
    def delete_one(cls,data):
        
        query = "DELETE FROM customers WHERE id = %(id)s;"
        
        connectToMySQL('users').query_db(query, data)
    
    @classmethod
    def update_one(cls, data):
        
        query = "UPDATE customers SET first_name = %(first_name)s, last_name = %(last_name)s, email_address = %(email_address)s WHERE id = %(id)s;"
        
        connectToMySQL('users').query_db(query, data)