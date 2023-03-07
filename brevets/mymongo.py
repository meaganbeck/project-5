from pymongo import MongoClient
import os

client = MongoClient('mongodb://' + os.environ['MONGODB_HOSTNAME'], 27017)
db = client.mydb
collection = db.controls


def get_control():
    controls = collection.find().sort("_id", -1).limit(1)
    for control in controls:
        return control["controls"], control["brevet_dist"], control["start_time"]

def set_control(brevet_dist, start_time, controls):
    output = collection.insert_one({"controls": controls, "brevet_dist":brevet_dist, "start_time":start_time})
    _id = output.inserted_id
    return str(_id)


@app.route('/insert/', method=['POST']) #where is this shit coming from?
def insert_brevet():
    try:
    open_time = request.json['open_time'],
    close_time = request.json['close_time'],
    km = request.json['km']

    controls_id = set_control(brevet_dist, start_time, controls)
    #db.insert_one(brevet_dist, start_time, controls)
        return flask.jsonify(
            result = {},
            status = 1,
            message = "inserted",
            mongo_id = controls_id)
    except:
        return flask.jsonify(
            result = {},
            status = 0,
            message = "naur. bad",
            mongo_id = 'None')
    

@app.route('/fetch')
def get_brevet():
    try:
        controls, brevet_dist, start_time = get_control()
    #brevet_dist, start_time, items = db.find(item_doc)
    
        return flask.jsonify(
            result = {'brevet_dist' : brevet_dist, 'start_time' : start_time, 'controls' : controls},
            status = 1,
            message = "got the data"
            )
    except:
        return flask.jsonify(result = {}, status = 0, message = "naur")


if __name__ == "__main__":
    app.run(port = 6661, host='0.0.0.0', debug=True) #maybe add port?
