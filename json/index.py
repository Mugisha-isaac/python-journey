import json

person = {"name": "John Doe", "age": 20, "nationality": "Canadian"}

# convert to json
jsonFormatted = json.dumps(person, indent=4, sort_keys=True)
print(jsonFormatted)
