import pytest
import requests

@pytest.fixture(scope='session')
def base_url():
    return "http://pulse-rest-testing.herokuapp.com"



# @pytest.fixture
# def book_data(base_url):
#     book_data = {"title": "My Book","author": "My Author"}
#
#     yield book_data
#     if 'id' in book_data:
#         requests.delete(f"{base_url}/books/{book_data['id']}")

# @pytest.fixture
# def wrong_book_data():
#     book_data = {"title": "My Book","author": ""}
#     return book_data

books_list = [{"title": "My Book","author": "Avtor"},
               {"title": "Boook","author": "Ator"},
              {"title": "66644", "author": "Atr"}
               ]

@pytest.fixture(params=books_list,ids=[str(x)for x in books_list])
def book_data(base_url, request):
    book_data = request.param
    yield book_data
    if 'id' in book_data:
        requests.delete(f"{base_url}/books/{book_data['id']}")