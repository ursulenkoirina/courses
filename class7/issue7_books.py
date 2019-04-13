import requests
import json
import unittest


class MyTest(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://pulse-rest-testing.herokuapp.com'
        self.book_id = None

    def test_create_book(self):
        book_data = {'title': 'LaDy With the DOG', 'author': 'Chekhov'}
        response = requests.post( self.base_url + "/books", data=book_data)
        self.assertEqual(response.status_code, 201)
        body = response.json()
        self.book_id = body.get('id')
        print(self.book_id)
        #1Bad
        # self.assertEqual(body.get('title'), book_data.get('title'))
        # self.assertEqual(body.get('author'), book_data.get('author'))

        #2
        # for key in book_data:
        #     self.assertEqual(body.get(key), book_data.get(key))

        book_data['id'] = self.book_id
        print(book_data)
        print(body)
        self.assertDictEqual(body, book_data)

    def tearDown(self):
        if self.book_id is not None:
            requests.delete(self.base_url + f"/books/{self.book_id}")


unittest.main(verbosity=2)