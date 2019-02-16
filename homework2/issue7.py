d = {'name': 'irina', 'age': 27, 'profession': 'engineer', 'city': 'kiev'}
d['age'] = d.get('age')+1
d['profession'] = 'doctor'
print(d)
print(d.values())
print(d.keys())