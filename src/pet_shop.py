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

def get_pets_by_breed(dict, pedigree):
    total_pets_in_breed = []
    for pet in dict['pets']:
        if pet['breed'] == pedigree:
            total_pets_in_breed.append(pet['breed'])
    return total_pets_in_breed

def find_pet_by_name(dict, pet_name):
    for pet in dict['pets']:
        if pet['name'] == pet_name:
            return pet

def remove_pet_by_name(dict, pet_name):
    for pet in dict['pets']:
        if pet['name'] == pet_name:
            dict['pets'].remove(pet)

def add_pet_to_stock(dict, new_pet):
    dict['pets'].append(new_pet)

def get_customer_cash(customer):
    return customer['cash']
    
def remove_customer_cash(customer, amount):
    customer['cash'] -= amount
        
def get_customer_pet_count(customer):
    if customer['pets'] == []:
        return 0
    else:
        return len(customer['pets'])

def add_pet_to_customer(customer, new_pet):
    customer['pets'].append(new_pet)

def customer_can_afford_pet(customer, new_pet):
    if customer['cash'] >= new_pet['price']:
        return True
    else:
        return False

 

   
