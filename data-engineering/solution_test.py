import unittest
import json
import solution

class TestSolution(unittest.TestCase):
    def test_inner_join_empty_right(self):
        left = [
            {'cid': 1, 'name': 'yolo'}
        ]
        right = []
        self.assertEqual(
            solution.inner_join(left, 'cid', right, 'customer_id'),
            [])


    def test_inner_join_one(self):
        left = [
            {'cid': 1, 'name': 'Karl'},
            {'cid': 2, 'name': 'Jim Bob'}
        ]
        right = [
            {'oid': 1, 'customer_id': 1, 'order': 'Pizza'}
        ]
        self.assertEqual(
            solution.inner_join(left, 'cid', right, 'customer_id'),
            [{'cid': 1, 'name': 'Karl', 'oid': 1, 'customer_id': 1, 'order': 'Pizza'}])


    def test_inner_join_dupes(self):
        left = [
            {'cid': 1, 'name': 'Karl'},
            {'cid': 2, 'name': 'Jim Bob'}
        ]
        right = [
            {'oid': 1, 'customer_id': 1, 'order': 'Pizza'},
            {'oid': 2, 'customer_id': 1, 'order': 'Shoes'}
        ]
        self.assertEqual(
            solution.inner_join(left, 'cid', right, 'customer_id'),
            [
                {'cid': 1, 'name': 'Karl', 'oid': 1, 'customer_id': 1, 'order': 'Pizza'},
                {'cid': 1, 'name': 'Karl', 'oid': 2, 'customer_id': 1, 'order': 'Shoes'}
            ]
        )


    def test_inner_join_empty_left(self):
        left = []
        right = [
            {'oid': 1, 'customer_id': 1, 'order': 'Pizza'}
        ]
        self.assertEqual(
            solution.inner_join(left, 'cid', right, 'customer_id'),
            [])


    def test_inner_join_empty_left_right(self):
        left = []
        right = []
        self.assertEqual(
            solution.inner_join(left, 'cid', right, 'customer_id'),
            [])


    def test_inner_join_no_matches(self):
        left = [
            {'cid': 1, 'name': 'Karl'},
            {'cid': 2, 'name': 'Jim Bob'}
        ]
        right = [
            {'oid': 1, 'customer_id': 3, 'order': 'pasta'},
            {'oid': 2, 'customer_id': 5, 'order': 'pop'}
        ]
        self.assertEqual(
            solution.inner_join(left, 'cid', right, 'customer_id'),
            [])

    def test_inner_join_multiple_matches(self):
        left = [
            {'cid': 1, 'name': 'Karl'},
            {'cid': 2, 'name': 'Jim Bob'},
            {'cid': 3, 'name': 'Fred'},
        ]
        right = [
            {'oid': 1, 'customer_id': 1, 'order': 'pasta'},
            {'oid': 3, 'customer_id': 3, 'order': 'pizza'},
            {'oid': 2, 'customer_id': 1, 'order': 'kale'},
            {'oid': 4, 'customer_id': 3, 'order': 'tuna'},
        ]
        self.assertEqual(
            solution.inner_join(left, 'cid', right, 'customer_id'),
            [
                {'cid': 1, 'name': 'Karl', 'oid': 1, 'customer_id': 1, 'order': 'pasta'},
                {'cid': 3, 'name': 'Fred', 'oid': 3, 'customer_id': 3, 'order': 'pizza'},
                {'cid': 1, 'name': 'Karl', 'oid': 2, 'customer_id': 1, 'order': 'kale'},
                {'cid': 3, 'name': 'Fred', 'oid': 4, 'customer_id': 3, 'order': 'tuna'},
            ])

    def test_inner_join_sample(self):
        left = [
            {
                'cid': 1,
                'name': 'Barry'
            },
            {
                'cid': 2,
                'name': 'Todd'
            },
            {
                'cid': 3,
                'name': 'Steve'
            },
            {
                'cid': 4,
                'name': 'Edward'
            },
            {
                'cid': 5,
                'name': 'Rodney'
            }
        ]
        right = [
            {
                'oid': 1,
                'customer_id': 1,
                'price': 2.5
            },
            {
                'oid': 2,
                'customer_id': 3,
                'price': 5
            },
            {
                'oid': 3,
                'customer_id': 3,
                'price': 2
            },
            {
                'oid': 4,
                'customer_id': 2,
                'price': 2
            },
            {
                'oid': 5,
                'customer_id': 6,
                'price': 3
            },
            {
                'oid': 6,
                'customer_id': 5,
                'price': 4
            },
            {
                'oid': 7,
                'customer_id': 1,
                'price': 10
            }
        ]
        self.assertEqual(
            solution.inner_join(left, 'cid', right, 'customer_id'),
            [
                {'cid': 1, 'name': 'Barry', 'oid': 1, 'customer_id': 1, 'price': 2.5},
                {'cid': 3, 'name': 'Steve', 'oid': 2, 'customer_id': 3, 'price': 5},
                {'cid': 3, 'name': 'Steve', 'oid': 3, 'customer_id': 3, 'price': 2},
                {'cid': 2, 'name': 'Todd', 'oid': 4, 'customer_id': 2, 'price': 2},
                {'cid': 5, 'name': 'Rodney', 'oid': 6, 'customer_id': 5, 'price': 4},
                {'cid': 1, 'name': 'Barry', 'oid': 7, 'customer_id': 1, 'price': 10}
            ]
        )
