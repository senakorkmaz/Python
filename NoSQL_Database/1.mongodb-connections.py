import pymongo

#myclient = pymongo.MongoClient('mongodb://localhost:27017')
myclient = pymongo.MongoClient('mongodb+srv://senanur:senanur@cluster0.33ohm.mongodb.net/node-app?retryWrites=true&w=majority')
mydb = myclient['node-app']
mycollection = mydb['products']

print(myclient.list_database_names())
print(mydb.list_collection_names())

product = {'name':'Samsung S5','price':2000}
result = mycollection.insert_one(product)

print(result)
print(type(result))
print(result.inserted_id)


