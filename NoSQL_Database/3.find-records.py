import pymongo

myclient = pymongo.MongoClient('mongodb+srv://senanur:senanur@cluster0.33ohm.mongodb.net/node-app?retryWrites=true&w=majority')

mydb = myclient['node-app']
mycollection = mydb['products']

#for one item
#result = mycollection.find_one()

#for all item in database
result = mycollection.find()

for item in result:
    print(item)

#only price and name
result = mycollection.find({},{'_id':0,'name':1,'price':1})

for item in result:
    print(item)

