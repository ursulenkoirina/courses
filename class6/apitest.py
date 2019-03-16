import requests
import json
url = 'http://pulse-rest-testing.herokuapp.com'
# r = requests.get(url+"/books")
r = requests.post(url+"/books",data={'title': 'LaDy With the DOG','author':'Chekhov'})
b =(r.json())
print(b['id'])
r3 = requests.delete(url+f"/books/{b['id']}")
r3 = requests.delete(url+"/books/" + str(b['id']))
print(r3.status_code)
# r3 = requests.delete()
# books = r.json()
# #Прочитать книги по автору
# for book in books:
#     print(book.get('author'))
#

