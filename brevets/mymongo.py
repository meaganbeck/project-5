from pymongo import MongoClient
import os

client = MongoClient('mongodb://' + os.environ['MONGODB_HOSTNAME'], 27017)
db = client.mydb
collection = db.items


def insert_brevet(brevet_dist, start_time, checkpoints):
    output = collection.insert_one({"checkpoints": checkpoints, "brevet_dist":brevet_dist, "start_time":start_time})
    _id = output.inserted_id
    return str(_id)

def get_brevet():
    items = collection.find().sort("_id", -1).limit(1)
    for item in itemss:
        return item["checkpoints"], item["brevet_dist"], item["start_time"]

if __name__ == "__main__":
    app.run(port = 6661, host='0.0.0.0', debug=True) #maybe add port?
