from pymongo import MongoClient
import os

client = MongoClient('mongodb://' + os.environ['MONGODB_HOSTNAME'], 27017)
db = client.mydb
collection = db.controls


def insert_brevet(brevet_dist, start_time, controls):
    output = collection.insert_one({"controls": controls, "brevet_dist":brevet_dist, "start_time":start_time})
    #_id = output.inserted_id
    return output

def get_brevet():
    controls = collection.find().sort("_id", -1).limit(1)
    for control in controls:
        return control["controls"], control["brevet_dist"], control["start_time"]

if __name__ == "__main__":
    app.run(port = 6661, host='0.0.0.0', debug=True) #maybe add port?
