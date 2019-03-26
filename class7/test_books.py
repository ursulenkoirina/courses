import unittest
import  requests


class BooksTesting(unittest.TestCase):
    def setUp(self):
        self.base_url = "http://pulse-rest-testing.herokuapp.com"
        self.book_id = None

    def test_book_create(self):
        book_data = {"title": "New Book",
                     "author": "New Author"}

        response = requests.post(f"{self.base_url}/books", data=book_data)
        self.assertEqual(201, response.status_code)
        body = response.json()
        self.book_id = body["id"]
        #1 BAD
        # self.assertEqual(body.get("title"), book_data.get("title"))
        # self.assertEqual(body.get("author"), book_data.get("author"))
        #2
        for key in book_data:
            self.assertEqual(body.get(key), book_data.get(key))
        #3
        book_data["id"] = self.book_id
        self.assertEqual(body, book_data)

    def tearDown(self):
        # if self.book_id is not None:
            requests.delete(f"{self.base_url}/books/" + self.book_id)
