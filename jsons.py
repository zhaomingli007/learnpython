import json

person = {"name": "John", "age": 30, "city": "New York",
          "hasChildren": False, "titles": ["engineer", "programmer"]}

with open('person.json', 'w') as file:
    json.dump(person,file, indent=4)

with open('person.json', 'r') as f:
    p = json.load(f)
    print(p)