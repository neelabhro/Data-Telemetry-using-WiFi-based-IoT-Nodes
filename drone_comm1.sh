#!/bin/bash
sleep 2
export ROS_IP=192.168.1.201
export ROS_MASTER_URI=http://192.168.1.200:11311
sleep 2
rosrun drone drone.py
#./chk_connection1.py
