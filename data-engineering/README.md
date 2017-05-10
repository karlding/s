# Data Engineering / Infrastructure Problem

## Problem

1. Build a simple joiner that accepts two files each containing an array of json objects. The user can specify any key that is shared in both files to join on.
1. Produce a new array with the joined objects. For simplicity follow the conventions of a standard SQL inner join, bonus points for implementing outer joins as well.
1. Try to keep runtime under ``O(n^2)``.
1. Join the supplied customers file to the supplied orders file. Using the keys `cid` and `customer_id` respectively.

**What to submit**: The length of the resulting array and the total for orders placed by Barry and Steve. 

## Solution

```bash
$ python solution.py
Length of the array is 6
The total is 19.5
```
