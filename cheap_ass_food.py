import ordrin
import random

ordrin_api = ordrin.APIs('GI2veJjbDGAu1eiraCCz12CcKKbviCa6lsWU4NrjgHk', ordrin.TEST)

def get_cheapest_food(addr, city, zip_code):
    #gives list of restaurant objects
    nb_list = ordrin_api.delivery_list('ASAP', addr, city, zip_code)

    #random restaurant index
    rand_restaurant_index = random.randint(0, len(nb_list)-1)

    #gets restaurant details for restaurant id
    rand_restaurant = ordrin_api.restaurant_details(str(nb_list[rand_restaurant_index]['id']))
    menu = rand_restaurant['menu']
    rid = rand_restaurant['restaurant_id']
    print 'Restaurant name: '+rand_restaurant['name']

    #list that wlil contain all the food items
    food_list = []

    for menu_item in menu:
        if menu_item['is_orderable'] == 1:
            for child in menu_item['children']:
                if child['is_orderable'] == 1:
                    if not child['price'] == '0.00':
                        food_list.append(child)

    try:
        cheapest_food = min(food_list, key = lambda child: child['price'])
    except ValueError:
        cheapest_food = None
        print 'No food found'

    return cheapest_food, rid

#takes in address of user and gets restaurant from cheapest food function
def make_delivery(addr, city, zip_code, em, first_name, last_name, phone, state, card_number, card_cvc, card_expiry, card_bill_addr, card_bill_city, card_bill_state, card_bill_zip, card_bill_phone):
    cheapest_food, rid = get_cheapest_food(addr, city, zip_code)
    delivery_check = ordrin_api.delivery_check('ASAP', rid, addr, city, zip_code)
    qty = 1
    if delivery_check['delivery'] == 1:
        print cheapest_food == None
        if not cheapest_food == None:
            print 'food id = '+cheapest_food['id']
            if not delivery_check['mino'] == '0.00':
                #order enough of the cheapest item to pass the min delivery charge
                qty = int(float(delivery_check['mino'])/float(cheapest_food['price'])) + 1
            ordrin_api.order_guest(rid, em, cheapest_food['id'] + '/' + str(qty), '0.00', first_name, \
                last_name, phone, zip_code, addr, city, state, card_number, card_cvc, card_expiry, \
                card_bill_addr, card_bill_city, card_bill_state, card_bill_zip, card_bill_phone, \
                addr2=None, card_name=None, card_bill_addr2=None, delivery_date='ASAP', \
                delivery_time=None)
        else:
            return None
    else:
        print 'This restaurant cannot deliver'

    print 'quantity '+str(qty)
    print 'Restaurant id '+rid
    return cheapest_food

def run():
    addr = str(raw_input("Please enter your address: "))
    city = str(raw_input("Please enter your city: "))
    zip_code = str(raw_input("Please enter your zipcode: "))
    em = str(raw_input("Please enter your email: "))
    first_name = str(raw_input("Please enter your first name: "))
    last_name = str(raw_input("Please enter your last name: "))
    phone = str(raw_input("Please enter your phone number: "))
    state = str(raw_input("Please enter your state: "))
    card_number = str(raw_input("Please enter your credit card#: "))
    card_cvc = str(raw_input("Please enter your security code: "))
    card_expiry = str(raw_input("Please enter your credit card expiration date: "))
    billing = str(raw_input("Is your credit card billing info the same as the above? Y/N\n"))
    if not billing.lower() == 'y':
        card_bill_city = str(raw_input("\nPlease enter your billing city: "))
        card_bill_addr = str(raw_input("Please enter your card billing address: "))
        card_bill_state = str(raw_input("Please enter your billing state: "))
        card_bill_zip = str(raw_input("Please enter your billing zip: "))
        card_bill_phone = str(raw_input("Please enter your billing phone: "))
    else:
        card_bill_addr = addr
        card_bill_city = city
        card_bill_state = state
        card_bill_zip = zip_code
        card_bill_phone = phone

    delivery = make_delivery(addr, city, zip_code, em, first_name, last_name, phone, state, card_number, card_cvc, card_expiry, card_bill_addr, card_bill_city, card_bill_state, card_bill_zip, card_bill_phone)
    if delivery:
        print delivery['name']
        print delivery['price']
    else:
        print "No freaking food jackpiss"

run()
