import json 

person_str = '{"name":"senanur","languages":["python","C#"] }'

#JSON string to dict
result = json.loads(person_str)
print(type(result))
print(result['name'])
print(result['languages'])

print('----------------')

#Dict to JSON string

person_dict = {
    "name":"Senanur",
    "languages":["python","java"]
}

result = json.dumps(person_dict)
print(result)
print(type(result))

#JSON dosyaya veri yazma (dict type)
with open('person.json','w') as f:
    json.dump(person_dict,f)

person_dict = json.loads(person_str)
print(person_dict)

result = json.dumps(person_dict,indent=4,sort_keys=True)
print(result)

#json dosyasindan veri alma (dict type)
# with open('person.json') as f:
#     data = json.load(f)
#     print(data['name'])
#     print(data['languages'])