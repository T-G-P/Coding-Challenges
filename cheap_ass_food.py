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

    return cheapest_food, rid

#takes in address of user and gets restaurant from cheapest food function
def make_delivery(addr, city, zip_code, em, first_name, last_name, phone, state, card_number, card_cvc, card_expiry, card_bill_addr, card_bill_city, card_bill_state, card_bill_zip, card_bill_phone):
    cheapest_food, rid = get_cheapest_food(addr, city, zip_code)
    delivery_check = ordrin.delivery_check('ASAP', rid, addr, city, zip_code)
    if delivery_check['delivery'] == 1:
        if not cheapest_food == None:
            if not delivery_check['mino'] == '0.00':
                #order enough of the cheapest item to pass the min delivery charge
                qty = int(float(delivery_check['mino'])/float(cheapest_food['price'])) + 1
                ordrin.order_guest(rid, em, cheapest_food['id'] + '/' + qty, tip, first_name, last_name, phone, zip_code, addr, city, state, card_number, card_cvc, card_expiry, card_bill_addr, card_bill_city, card_bill_state, card_bill_zip, card_bill_phone, addr2=None, card_name=None, card_bill_addr2=None, delivery_date='ASAP', delivery_time=None)
