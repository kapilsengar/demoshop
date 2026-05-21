import random


def get_login_data():

    email = "squad11@gmail.com"
    password = "Pass@123"

    return email, password




def get_register_data():

    random_number = random.randint(1000, 99999)

    first_name = "Selenium"
    last_name = "Squad"
    email = f"selenium{random_number}@gmail.com"
    password = "Pass@123"

    return first_name, last_name, email, password

def get_invalid_login_data():

    email = "invalid@gmail.com"
    password = "invalid"

    return email, password