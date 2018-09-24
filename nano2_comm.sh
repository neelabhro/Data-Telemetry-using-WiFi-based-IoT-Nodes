#!/bin/bash
roscore &
export ROS_IP=192.168.1.202
export ROS_MASTER_URI=http://192.168.1.202:11311
sleep 2
rosrun comm nanostation2.py
sleep 2
killall -9 rosmaster
#sleep 2
#sleep 5
#./check_connection.py
