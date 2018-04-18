import pymongo
import pprint
from pymongo import MongoClient

client = MongoClient()
database = client.test

collection = database.movies

collection2 = database.school
collection3 = database.gym

database.collection.update_many(
    {"rated":"NOT RATED"},
    {"$set": {"rated":"Pending rating"}}
)


database.collection.insert_one(
    {"title": "Jumanji: Welcome to the Jungle",
     "year": 100,
     "countries": ["France", "USA", "Germany", "UK", "United Arab Emirates"],
     "genres":["Action", "Adventures", "Comedy", "Fantasy"],
     "directors":["Jake Kasdan"],
     "imdb":[
     {
        "id": 123,
        "rating": 7.0,
        "votes" : 3,}]})
pipeline1 = [
    {"$unwind": "$genres"},
    {"$group": {"_id": "$genres", "count": {"$sum": 1}}} ]
pprint.pprint(list(database.collection.aggregate(pipeline1)))

pipeline2 = [
    {"$unwind": "$countries"},
    {"$group": {"_id": "$countries", "count": {"$sum": 1}}}
    ]
pprint.pprint(list(database.collection.aggregate(pipeline2)))



