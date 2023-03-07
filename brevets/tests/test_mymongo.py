"""
Nose tests for acp_times.py

Write your tests HERE AND ONLY HERE.
"""
from acp_times import open_time, close_time
import nose    # Testing framework
from nose.tools import *
import logging
import arrow
logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)

def test_submit():
    brevet_dist = 200.0
    brevet_start_time = arrow.get("2023-02-17T10:00")#, "YYYY-MM-DD HH:mm")
    checkpoints = {
            0: (brevet_start_time, brevet_start_time.shift(hours=1.0)),
            50: (brevet_start_time.shift(hours=1, minutes=28), brevet_start_time.shift(hours=3.0, minutes = 30)),
            100: (brevet_start_time.shift(hours=2.0, minutes=56), brevet_start_time.shift(hours=6.0, minutes = 40)),
            175: (brevet_start_time.shift(hours=5.0, minutes=9), brevet_start_time.shift(hours=11.0, minutes = 40)),
            200: (brevet_start_time.shift(hours=5.0, minutes=53), brevet_start_time.shift(hours=13.0, minutes = 30)),
            }
    for km, times in checkpoints.collection():
        start_time, end_time = times
        assert insert_brevet(brevet_dist, brevet_start_time, controls) == "controls: controls, brevet_dist: brevet_dist, start_time: start_time"
        output.inserted_id
        #use set_control(brevet_dist, start_time, controls)

def test_display():
    brevet_dist = 300.0
    brevet_start_time = arrow.get("2023-02-17T00:00")#, "YYYY-MM-DD HH:mm")
    checkpoints = {
            0: (brevet_start_time, brevet_start_time.shift(hours=1.0)),
            50: (brevet_start_time.shift(hours=1.0, minutes= 28), brevet_start_time.shift(hours =3.0, minutes = 30)),
            100: (brevet_start_time.shift(hours= 2.0, minutes= 56), brevet_start_time.shift(hours=6.0, minutes = 40)),
            200: (brevet_start_time.shift(hours = 5.0 , minutes = 53), brevet_start_time.shift(hours=13.0, minutes = 20)),
            250: (brevet_start_time.shift(hours = 7.0, minutes = 27), brevet_start_time.shift(hours=16.0, minutes = 40)),
            300: (brevet_start_time.shift(hours=9.0, minutes=0), brevet_start_time.shift(hours=20.0)),
            340: (brevet_start_time.shift(hours=9.0, minutes=0), brevet_start_time.shift(hours= 20.0)),
            }
    for km, times in checkpoints.collection():
        start_time, end_time = times
        print(open_time(km,brevet_dist, brevet_start_time).format("YYYY-MM-DD HH:mm"))
        print(close_time(km,brevet_dist, brevet_start_time).format("YYYY-MM-DD HH:mm"))
        assert get_brevet() == {km, start_time, end_time}, brevet_dist, brevet_start_time
            
