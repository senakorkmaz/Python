import requests
import json

apiUrl = 'http://data.fixer.io/api/latest?access_key=73bcfeaccc2759489ab7566ce315c8f1&format=1'
dovizBilgi = requests.get(apiUrl)
dovizBilgi = json.loads(dovizBilgi.text)

#print(dovizBilgi)
bozulan_doviz = input('Bozulan doviz turu:')
alinan_doviz = input('Alinan doviz turu:')
miktar = int(input(f'Ne kadar {bozulan_doviz} bozdurmak istiyorsunuz:'))
aMiktar = dovizBilgi['rates'][alinan_doviz]
bMiktar = dovizBilgi['rates'][bozulan_doviz]
kalanMiktar = int((float(aMiktar)/float(bMiktar))*miktar)
print(f'{kalanMiktar} kadar {alinan_doviz} aldiniz.')