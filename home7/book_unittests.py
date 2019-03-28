import unittest
import requests

from funcs import check_dict_by_id

class BooksTesting(unittest.TestCase):
    def setUp(self):
        self.base_url = "http://pulse-rest-testing.herokuapp.com/books/"
        self.book_id = None

    def test_book_create(self):
        book_data = {"title": "LaDy With the DOG",
                     "author": "Chekhov"}

        response = requests.post(f"{self.base_url}", data=book_data)
        self.assertEqual(201, response.status_code)
        body = response.json()
        self.book_id = body.get("id")
        book_data["id"] = self.book_id
        self.assertEqual(body, book_data)

        request_get_by_id = requests.get(f"{self.base_url}" + str(self.book_id))
        self.assertEqual(200, request_get_by_id.status_code)

        request_get_all = requests.get(f"{self.base_url}")
        all_books = request_get_all.json()
        self.assertIsNotNone(check_dict_by_id(self.book_id, all_books))

        update = requests.put(f"{self.base_url}{self.book_id}", data={'author': 'Alex'})
        self.assertEqual(200,update.status_code)

        request_get_all = requests.get(f"{self.base_url}")
        all_books = request_get_all.json()
        self.assertEqual('Alex', check_dict_by_id(self.book_id, all_books).get('author'))

        requests.delete(f"{self.base_url}" + str(self.book_id))
        request_del = requests.get(f"{self.base_url}" + str(self.book_id))
        self.assertEqual(404, request_del.status_code)

        request_get_all = requests.get(f"{self.base_url}")
        all_books = request_get_all.json()
        self.assertIsNone(check_dict_by_id(self.book_id, all_books))


    def tearDown(self):
        if self.book_id is not None:
            requests.delete(f"{self.base_url}" + str(self.book_id))
