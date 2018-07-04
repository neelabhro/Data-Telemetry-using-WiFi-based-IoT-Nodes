#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
import glob
import os

img_dir = "/home/sauranil/Desktop/img_folder"
data_path = os.path.join(img_dir, '*g')
files = glob.glob(data_path)

def main():
	rospy.init_node("image_sender", anonymous = True)
	image_pub = rospy.Publisher('image_topic', Image, queue_size = 10)
	bridge = CvBridge()

	rate = rospy.Rate(1)

	while not rospy.is_shutdown():
		for f1 in files:
			print(f1)
			img = cv2.imread(f1)
			image_pub.publish(bridge.cv2_to_imgmsg(img, "bgr8"))
			rate.sleep()

if __name__ == '__main__':
	try:
		main()
	except rospy.ROSInterruptException:
		pass