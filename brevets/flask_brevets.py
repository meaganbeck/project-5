"""
Replacement for RUSA ACP brevet time calculator
(see https://rusa.org/octime_acp.html)

"""

import flask
from flask import request
import arrow  # Replacement for datetime, based on moment.js
import acp_times  # Brevet time calculations
from mymongo import insert_brevet, get_brevet
import config

import logging

###
# Globals
###
app = flask.Flask(__name__)
CONFIG = config.configuration()

###
# Pages
###


@app.route("/")
@app.route("/index")
def index():
    app.logger.debug("Main page entry")
    return flask.render_template('calc.html')

###############
#
# AJAX request handlers
#   These return JSON, rather than rendering pages.
#
###############
@app.route("/_calc_times")
def _calc_times():
    """
    Calculates open/close times from miles, using rules
    described at https://rusa.org/octime_alg.html.
    Expects one URL-encoded argument, the number of miles.
    """
    app.logger.debug("Got a JSON request")
    km = request.args.get('km', 999, type=float)
    brevet_distance = request.args.get('brevet_distance', 999, type=float)#dded
    start_time = request.args.get('start_time', type=str) #added. passes to acp times. convert to arrow object before passing below in open/close times. 
    app.logger.debug("km={}".format(km))
    app.logger.debug("brev_dist={}".format(brevet_distance))
    app.logger.debug("start_time={}".format(start_time))
    app.logger.debug("request.args: {}".format(request.args))
     #FIXME!
     #Right now, only the current time is passed as the start time
     #and control distance is fixed to 200
     #You should get these from the webpage!
    open_time = acp_times.open_time(km, brevet_distance, arrow.get(start_time, 'YYYY-MM-DDTHH:mm'))
    close_time = acp_times.close_time(km, brevet_distance, arrow.get(start_time, 'YYYY-MM-DDTHH:mm')) #maybe end_time...
    result = {"open": open_time, "close": close_time}
    return flask.jsonify(result=result)


@app.route('/insert/', method=['POST']) #where is this shit coming from?
def insert(brevet_dist, start_time, checkpoints):
    checkpoints = request.json['checkpoints']
    start_time = request.json['start_time']
    brevet_dist = request.json['brevet_dist']

    checkpoints_id = insert_brevet(brevet_dist, start_time, checkpoints)
    #db.insert_one(brevet_dist, start_time, controls)
        return flask.jsonify(
            result = {},
            status = 1,
            message = "inserted",
            mongo_id = checkpoints_id)
    except:
        return flask.jsonify(
            result = {},
            status = 0,
            message = "Server error",
            mongo_id = 'None')
    

@app.route('/fetch')
def fetch():
    try:
        checkpoints, brevet_dist, start_time = get_brevet()
    #brevet_dist, start_time, items = db.find(item_doc)
    
        return flask.jsonify(
            result = {'brevet_dist' : brevet_dist, 'start_time' : start_time, 'checkpoints' : checkpoints},
            status = 1,
            message = "got the data"
            )
    except:
        return flask.jsonify(result = {"brevet_dist": 200, "start_time": arrow.now().format("YYY-MM-DDTHH:mm"), "checkpoints": []}, status = 0)

app.debug = CONFIG.DEBUG
if app.debug:
    app.logger.setLevel(logging.DEBUG)

if __name__ == "__main__":
    print("Opening for global access on port {}".format(CONFIG.PORT))
    app.run(port=CONFIG.PORT, host="0.0.0.0")
