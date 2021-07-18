from mysqlconnection import connectToMySQL

class Customers():
    
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email_address = data['email_address']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def new_customer(cls, data):
        
        query = "INSERT INTO customers (first_name, last_name, email_address) VALUES (%(first_name)s, %(last_name)s, %(email_address)s);"
        
        return connectToMySQL('users').query_db(query, data)
        

    @classmethod 
    def display_list(cls):
        
        query = "SELECT * FROM customers;"
        
        results = connectToMySQL('users').query_db(query)
        
        customers = []
        
        for customer in results:
            customers.append(cls(customer))

        return customers
