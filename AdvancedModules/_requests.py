import requests
import json
result = requests.get('https://jsonplaceholder.typicode.com/todos')
print(result)

bilgi = result.text
print(bilgi)
print(type(bilgi))

#bilgiyi dict veri tipine donusturduk
cevirilmis = json.loads(bilgi)
print(type(cevirilmis))
for i in cevirilmis:
    print(i)

#cevirilen bilgilerin sadece bir ozelligini bastirmak istersek
for i in cevirilmis:
    print(i['title'])