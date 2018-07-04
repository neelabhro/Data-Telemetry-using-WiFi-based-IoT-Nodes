#!/bin/bash
export ROS_IP=192.168.1.202
export ROS_MASTER_URI=http://192.168.1.200:11311
sleep 2
rosrun comm image_receiver.py