person = {
    'name': 'Rajender',
    'age': 26,
    'city': 'Hyderabad'
}


# print(person.keys())
# print(person['name'])
# print(person)

person['email'] = 'rajender@example.com'

# print(person.get('name'))
# person(person.get('salary'))

print(person.get('salary', 0))


for key,  val in person.items():
    print(key, val)
