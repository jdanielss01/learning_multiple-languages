import pymongo


pwd = "yqodMEdbPJqjz2Ep"
user = "2023josesalinas"
cluster = "clusterjose.hhigppk"
uri = f"mongodb+srv://{user}:{pwd}@{cluster}.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(uri)


"""
# RECOGER DB
"""
#--1
#db = client.get_database("alumnes")
#--2 (default)
# db = client['alumnes']
#--3
db = client.animales


"""
# RECOGER COLECCIONES (tablas)
"""
#--1
colection = db.get_collection("osos")
#--2 (default)
#colection = db['alumnes']
#--3
#colection = db.alumnes?
#print(colection)


## RECOGER DOCUMENTO/s(REGISTRO/s) (QUERYS)

#--1
res = colection.find_one()
#--2 (default)
#db_animales.osos.insert_one({"nombre":"leon"})

#res = colection
#print(res)
#db.

client.close()
        
