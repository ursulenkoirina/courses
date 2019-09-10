"""
Задание 1 (Обязательное всем!!!!)
Тестовое приложение с REST API  http://pulse-rest-testing.herokuapp.com/
Создаём один скрипт:
1.1	Создаёт персонажа POST /roles/, вы запоминаете его id.
1.2	Проверяете, что он создался и доступен по ссылке GET /roles/[id]
1.3	Проверяете, что он есть в списке пользователей по GET /roles/
1.4	Изменяете этого пользователя методом PUT roles/[id]/
1.5	Проверяете, что он изменился и доступен по ссылке /roles/[id]
1.6	Проверяете, что он есть в списке пользователей по GET /roles/ с новой инфой
1.7	Удаляете этого пользователя методом DELETE roles/[id]
Второй скрипт: тоже самое с книгами
** Попробуйте воспользоваться http.client вместо requests. Ощутите разницу 😊
"""
import requests
import json
url = 'http://pulse-rest-testing.herokuapp.com'
r = requests.post(url+"/roles", data={'name': 'Sergey', 'type': 'IT', 'level':'20', 'book':'145'})
b = r.json()
r_id = b.get('id')
assert r.status_code == 201,  "Role wasn't created error is ".format(r.status_code)
r_get_id = requests.get(url+f"/roles/{r_id}")
assert r_get_id.status_code == 200, " Role isn't available by id error is ".format(r_get_id.status_code)
r_get = requests.get(url+f"/roles/")
l = r_get.json()

def check_dict_by_id(r_id,l):
    new_dict = None
    for i in l:
        if i.get('id') == r_id:
            new_dict = i
    return new_dict

assert check_dict_by_id(r_id, l) != None , "Role with id {} was not found".format(r_id)

r_update = requests.put(url+f"/roles/{r_id}", data={'level': '100'})
r_get_id = requests.get(url+f"/roles/{r_id}")
assert r_get_id.status_code == 200, " Role isn't available by id error is ".format(r_get_id.status_code)
r_get = requests.get(url+f"/roles/")
l = r_get.json()
assert check_dict_by_id(r_id, l).get('level') == 100, " Role isn't update with new information"
r3 = requests.delete(url+f"/roles/{r_id}")
r3 = requests.delete(url+"/roles/342")
assert r3.status_code == 204, 'Role isn"t deleted with {}'.format(r_id)
