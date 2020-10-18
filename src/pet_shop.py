# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(dict):
    return (dict['name'])

def get_total_cash(dict):
    return (dict['admin']['total_cash'])

def add_or_remove_cash(dict, amount):
    dict['admin']['total_cash'] += amount
    
def get_pets_sold(dict):
    return (dict['admin']['pets_sold'])

def increase_pets_sold(dict, amount):
    dict['admin']['pets_sold'] += amount

def get_stock_count(dict):
    return len(dict['pets'])

    
