import json
from decimal import Decimal, ROUND_HALF_UP


def inner_join(left, left_key, right, right_key):
    # ensure that the smaller dict is on the left
    if len(left) > len(right):
        left, right = right, left
        left_key, right_key = right_key, left_key

    hashmap = {}
    joined = []

    # add the smaller dict to hashmap
    for ele in left:
        hashmap[ele[left_key]] = ele

    # for each element in the larger dict, check if the key exists
    for ele in right:
        if ele[right_key] in hashmap:
            datum = dict(hashmap[ele[right_key]])
            datum.update(ele)

            joined.append(datum)

    return joined


def main():
    customers = []
    orders = []

    with open('customers.json') as json_data:
        customers = json.load(json_data)

    with open('orders.json') as json_data:
        orders = json.load(json_data)

    results = inner_join(customers, 'cid', orders, 'customer_id')
    print("Length of the array is %s" % len(results))

    total = 0
    for order in results:
        if order['name'] in ['Barry', 'Steve']:
            cents = Decimal(order['price'])
            total = total + cents
    print("The total is %s" % total.quantize(total, ROUND_HALF_UP))


if __name__ == '__main__':
    main()
