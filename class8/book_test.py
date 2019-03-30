import requests
import pytest

def test_book_create(base_url, book_data):
    response = requests.post(f"{base_url}/books", data=book_data)
    assert 201 == response.status_code
    body = response.json()
    book_data["id"] = body['id']
    assert body == book_data


# # @pytest.mark.skip(reason='ddd')
# # @pytest.mark.xfail
# @pytest.mark.xfail(raises=(ValueError,AssertionError), strict=True)
# def test_neg_book_create(base_url, wrong_book_data):
#     response = requests.post(f"{base_url}/books", data=wrong_book_data)
#     # raise ValueError('not correct')
#     assert 404 == response.status_code
#     body = response.json()
#     assert body == {'author': ['This field may not be blank.']}
#     # if body.get('id'):
#     #     wrong_book_data['id'] = body['id']


wrong_books_list = [
    ({"title": "My Book",
      "author": ""},
     {'author': ['This field may not be blank.']}
     ),
     ({"title": "","author": "Autor"},
      {'title': ['This field may not be blank.']}
            )
               ]
# # @pytest.mark.parametrize('wrong_book_data, expected_body', wrong_books_list, ids=["empty autor","empty title"])
# @pytest.mark.parametrize('wrong_book_data, expected_body', wrong_books_list, ids=[str(x[0])for x in wrong_books_list])
# def test_neg_book_create(base_url, wrong_book_data,expected_body):
#     response = requests.post(f"{base_url}/books", data=wrong_book_data)
#     # raise ValueError('not correct')
#     assert 400 == response.status_code
#     body = response.json()
#     # assert body == {'author': ['This field may not be blank.']}
#     # assert ['This field may not be blank.'] in body.values()
#     assert expected_body == body
#     # if body.get('id'):
#     #     wrong_book_data['id'] = body['id']



books_list = [{"title": "My Book","author": "Avtor"},
               {"title": "Boook","author": "Ator"},
              {"title": "44", "author": "Atr"}
               ]

@pytest.mark.parametrize('book_data_new', books_list,ids=[str(x)for x in books_list])
def test_book_create(base_url, book_data_new):
    response = requests.post(f"{base_url}/books", data=book_data_new)
    assert 201 == response.status_code
    body = response.json()
    book_data_new["id"] = body['id']
    assert body == book_data_new