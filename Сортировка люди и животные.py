import json

with open('people.json', encoding="utf8") as f:
    people = json.load(f)
    
people = sorted(people, key=lambda s: s['animal'])

with open('animal.json', encoding="utf8") as f:
    animal = json.load(f)
    
animal = sorted(animal, key=lambda s: s['animal'])

print(people, animal)
