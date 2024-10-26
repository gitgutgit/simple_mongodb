
import toml
from pymongo import MongoClient


# Load MongoDB URL from secrets.toml
config = toml.load("secrets.toml")
URL = config["database"]["url"]


# Connect to MongoDB (assuming MongoDB is running locally)

# URLEXAMPLE  = "mongodb+srv://<dbname>:<dbpassword>@cluster0.t5abf.mongodb.net/"
client = MongoClient(URL)

# Select the database and collection
db = client["gaming_database"]
gamers_collection = db["gamers"]

# Example data for a gamer
gamer_data = {
    "_id": 123,  # Using gamer ID as the unique identifier
    "name": "Alex",
    "age": 27,
    "region": "New York",
    "address": "123 Gamer Street, NY",
    "current_games": ["Fortnite", "Apex Legends"],
    "past_games": ["Call of Duty", "League of Legends"],
    "achievements": [
        {"achievement_name": "Victory Royale", "date": "2024-08-15"},
        {"achievement_name": "Legendary Rank", "date": "2024-09-01"}
    ]
}

# Insert the gamer data into MongoDB

# Check if a document with the same _id already exists
if gamers_collection.find_one({"_id": gamer_data["_id"]}):
    print("A gamer with this ID already exists. Insertion canceled.")
else:
    # Insert the gamer data into MongoDB
    result = gamers_collection.insert_one(gamer_data)
    print("Data inserted with id:", result.inserted_id)


