import pymongo as db

myclient = db.MongoClient("mongodb://localhost:27017")

mydb = myclient["mydatabase"]

print(myclient.list_database_names())

dblist = myclient.list_database_names()
if "mydatabase" in dblist:
    print("The database exists.")

#! Crie uma coleção chamada "clientes"
myclient = db.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]

mycol = mydb["customers"]
print(mydb.list_collection_names())

collist = mydb.list_collection_names()
if "customers" in collist:
    print("The collection exists.")

#! Classifique o resultado reverso em ordem alfabética por nome:
myclient = db.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

mydoc = mycol.find().sort("name", -1)

for x in mydoc:
    print(x)
