import math
import json
import grequests

URL = ['https://backend-challenge-fall-2017.herokuapp.com/orders.json']


def get_num_pages(pagination_data):
    curr = pagination_data['current_page']
    per_page = pagination_data['per_page']
    total = pagination_data['total']

    return math.ceil(total / (curr * per_page))


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
    request = (grequests.get(u) for u in URL)
    response = grequests.map(request)
    data = [r.json() for r in response]
    data = data[0]

    output = {'remaining_cookies': data['available_cookies'], 'unfulfilled_orders': []}
    urls = [URL[0] + "?page=%d" % i for i in range(1, get_num_pages(data['pagination']) + 1)]

    requests = (grequests.get(u) for u in urls)
    responses = grequests.map(requests)
    result = [r.json() for r in responses]

    orders = []
    for order in result:
        orders.extend(order['orders'])

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
