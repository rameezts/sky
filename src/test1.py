from flask import request
def get_url_params():
    ## you might further need to format the URL params through escape.    
    firstName = request.args.get('first_name') 
    return firstName
