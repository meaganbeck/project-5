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
        assert insert_brevet(brevet_dist, brevet_start_time, controls) == f"{{km},{start_time}, {end_time}}, {brevet_dist},{brevet_start_time}"
        #output.inserted_id
        #use set_control(brevet_dist, start_time, controls)

def test_display():
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
        assert get_brevet() == {km, start_time, end_time}, brevet_dist, brevet_start_time
            
