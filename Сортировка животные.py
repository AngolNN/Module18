import json

with open('animal.json', encoding="utf8") as f:
    animal = json.load(f)
    
animal = sorted(animal, key=lambda s: s['animal'])

print(animal)
