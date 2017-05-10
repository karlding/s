# Backend

## Problem

One Shopify merchant bakes tasty treats and sells them locally, but they haven’t been able to bake cookies fast enough to keep up with the demand of all the orders.  Because of this, they have asked for your help to organize all cookie orders, so they can see which orders they will need to bake more cookies for.

You have a limited amount of cookies remaining and a list of orders. The merchant needs to know which orders will not be *fulfilled after following the requirements specified below.

**order fulfillment**: The process between when a merchant receives an order from a customer and delivers the product into the customer's hands.

You have access to a paginated API in: https://backend-challenge-fall-2017.herokuapp.com/orders.json 
where you can obtain all the orders. The API accepts a `page` parameter, example: https://backend-challenge-fall-2017.herokuapp.com/orders.json?page=2

### Requirements

1. Read all orders from the paginated API.
1. Any order without cookies can be fulfilled.
1. Prioritize fulfilling orders with the highest amount of cookies.
1. If orders have the same amount of cookies, prioritize the order with the lowest ID.
1. If an order has an amount of cookies bigger than the remaining cookies, skip the order.

### What to submit:

Output (in JSON)

```json
{
  "remaining_cookies": "Amount of cookies remaining after trying to fulfill orders",
  "unfulfilled_orders": [ "IDs of the order that couldn't be fulfilled in ascending order" ]
}
```


### Example Answer Output

```json
{
  "remaining_cookies": 0,
  "unfulfilled_orders": [ 3, 5 ]

}
```

## Solution

```bash
$ pip install -r requirements.txt
$ python solution.py
```

```json
{
  "remaining_cookies": 0,
  "unfulfilled_orders": [8, 7, 11]
}
```
