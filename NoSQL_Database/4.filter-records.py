import pymongo
from bson.objectid import ObjectId

myclient = pymongo.MongoClient('mongodb+srv://senanur:senanur@cluster0.33ohm.mongodb.net/node-app?retryWrites=true&w=majority')

mydb = myclient['node-app']
mycollection = mydb['products']

filter = {'name':'Samsung S5'}

result = mycollection.find(filter,{'_id':0,'price':1})
for item in result:
    print(item)

print('-------------------------------')
filterId = {'_id':ObjectId('61fc1d9ed4f4ba28cd251ab0')}
result2 = mycollection.find_one(filterId)
print(result2)

print('-------------------------------')
result3 = mycollection.find({
    'name':{
        '$in':['Samsung S5','Samsung S6']
    }
})
for item in result3:
    print(item)

print('-------------------------------')
result4 = mycollection.find({
    'price':{
        '$gte':6000
    }
})
for item in result4:
    print(item)

print('-------------------------------')
result5 = mycollection.find({
    'price':{
        '$eq':6000
    }
})
for item in result5:
    print(item)

print('-------------------------------')
result6 = mycollection.find({
    'price':{
        '$lte':2000
    }
})
for item in result6:
    print(item)

print('-------------------------------')
result7 = mycollection.find({
    '$and':[
        {
            'price':{
                '$gte':3000
            }
        },
        {
            'name':{

                '$in':['Samsung S5','Samsung S6']
            }
        }
    ]
})
for item in result7:
    print(item)

print('-------------------------------')
result8= mycollection.find({
    'name':{
        '$regex':'^S'
    }
})
for item in result8:
    print(item)

print('-------------------------------')
result9= mycollection.find({
    'name':{
        '$regex':'S7$'
    }
})
for item in result9:
    print(item)