import pymongo

#myclient = pymongo.MongoClient('mongodb://localhost:27017')
myclient = pymongo.MongoClient('mongodb+srv://senanur:senanur@cluster0.33ohm.mongodb.net/node-app?retryWrites=true&w=majority')
mydb = myclient['node-app']
mycollection = mydb['products']

productList = [
    {'name':'Samsung S6','price':3000,'description':'iyi telefon'},
    {'name':'Samsung S7','price':4000,'categories':['telefon','elektronik']}
]

results = mycollection.insert_many(productList)
print(results.inserted_ids)