import math
import requests
import json

URL = 'https://backend-challenge-fall-2017.herokuapp.com/orders.json'


def get_num_pages(pagination_data):
    curr = pagination_data['current_page']
    per_page = pagination_data['per_page']
    total = pagination_data['total']

    return math.ceil(total / (curr * per_page))


def get_page(page):
    payload = {'page': page}
    r = requests.get(URL, params=payload)
    return r.json()


def unfulfilled_order_contains_cookies(order):
    if order['fulfilled'] == True:
        return False
    for product in order['products']:
        if product['title'] == 'Cookie':
            return True
    return False


def order_num_cookies(order):
    for product in order['products']:
        if product['title'] == 'Cookie':
            return product['amount']
    return 0


def order_key(order):
    return order_num_cookies(order), order['id'] * -1


def main():
    r = requests.get(URL)
    data = r.json()
    output = {'remaining_cookies': data['available_cookies'], 'unfulfilled_orders': []}
    orders = []
    for i in range(get_num_pages(data['pagination'])):
        page = get_page(i + 1)
        orders.extend(page['orders'])

    cookie_orders = list(filter(unfulfilled_order_contains_cookies, orders))
    cookie_orders = sorted(cookie_orders, key=order_key, reverse=True)

    for order in cookie_orders:
        num_cookies = order_num_cookies(order)
        if num_cookies > output['remaining_cookies']:
            output['unfulfilled_orders'].append(order['id'])
        else:
            output['remaining_cookies'] = output['remaining_cookies'] - num_cookies

    print(json.dumps(output))


if __name__ == '__main__':
    main()
