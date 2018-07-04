#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge, CvBridgeError

bridge = CvBridge()
i = 0

def callback(msg):
	global i
	print("Receiving image")
	try:
		cv2_img = bridge.imgmsg_to_cv2(msg, "bgr8")
	except CvBridgeError, e:
		print(e)
	else:
		cv2.imwrite("/home/neelabhro/Desktop/saved_img_folder/image%i.jpg"%i, cv2_img)
	i += 1

def main():
	print("#####")
	rospy.init_node('image_receiver')
	rospy.Subscriber('image_topic', Image, callback)
	rospy.spin()

if __name__ == '__main__':
	try:
		main()
	except rospy.ROSInterruptException:
		pass