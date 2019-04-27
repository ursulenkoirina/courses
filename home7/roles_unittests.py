import unittest
import requests

from funcs import check_dict_by_id

class RolesTesting(unittest.TestCase):
    def setUp(self):
        self.base_url = "http://pulse-rest-testing.herokuapp.com/roles/"
        self.role_id = None

    def test_role_create(self):
        role_data = {'name': 'Sergey', 'type': 'IT', 'level': 20, 'book': 2187}
        response = requests.post(self.base_url, data=role_data)
        self.assertEqual(201, response.status_code)
        body = response.json()
        self.role_id = body.get("id")
        role_data["id"] = self.role_id
        self.assertEqual(body, role_data)

        request_get_by_id = requests.get(self.base_url + str(self.role_id))
        self.assertEqual(200, request_get_by_id.status_code)

        request_get_all = requests.get(self.base_url)
        all_roles = request_get_all.json()
        self.assertIsNotNone(check_dict_by_id(self.role_id, all_roles))

        update = requests.put(self.base_url + str(self.role_id), data={'type': 'QA'})
        self.assertEqual(200,update.status_code)

        request_get_all = requests.get(self.base_url)
        all_roles = request_get_all.json()
        self.assertEqual('QA', check_dict_by_id(self.role_id, all_roles).get('type'))

        requests.delete(self.base_url + str(self.role_id))
        request_del = requests.get(self.base_url + str(self.role_id))
        self.assertEqual(404, request_del.status_code)

        request_get_all = requests.get(self.base_url)
        all_roles = request_get_all.json()
        self.assertIsNone(check_dict_by_id(self.role_id, all_roles))


    def tearDown(self):
        if self.role_id is not None:
            requests.delete(f"{self.base_url}" + str(self.role_id))
