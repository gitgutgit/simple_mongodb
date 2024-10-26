from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Select the database and collection
db = client["gaming_database"]
gamers_collection = db["gamers"]

# Function to retrieve a gamer's data by ID
def get_gamer_data(gamer_id):
    gamer = gamers_collection.find_one({"_id": gamer_id})
    if gamer:
        return gamer
    else:
        return f"No gamer found with ID {gamer_id}"

# Example usage
if __name__ == "__main__":
    gamer_id = 123  # Replace with the gamer ID you want to retrieve
    gamer_data = get_gamer_data(gamer_id)
    print(gamer_data)
