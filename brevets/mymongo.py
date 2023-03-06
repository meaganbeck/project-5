from pymongo import MongoClient
import os

client = MongoClient('mongodb://' + os.environ['MONGODB_HOSTNAME'], 27017)
db = client.mydb


@app.route('/insert/', method=['POST']) #where is this shit coming from?

def insert_brevet(brevet_dist, start_time, controls):
    items= {#open close, controls
            'open_time': request.json['open_time'],
            'close_time' : request.json['close_time'],
            'km'   : request.json['km']
            }
    db.insert_one(brevet_dist, start_time, controls, items)
    pass

@app.route('/fetch')
def get_brevet():
    brevet_dist, start_time, controls, items = db.find(item_doc)
    
    return flask.jsonify(
            result = {'brevet_dist' : brevet_dist, 'start_time' : start_time, 'controls' : controls, 'items' : items}
            )

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
