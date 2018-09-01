#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
import glob
import os

img_dir = "/home/sauranil/Desktop/Communication_Summer/drone/send_folder"
data_path = os.path.join(img_dir, '*g')
files = glob.glob(data_path)
count = 0
i = 0
loop = 0
length = len(files)
n = 0
flag = 0
flag1 = 0
flag2 = 0

bridge = CvBridge()

def callback1(msg):
	global i
	print("receiving image from nanostation 1")
	try:
		cv2_img = bridge.imgmsg_to_cv2(msg, "bgr8")
	except CvBridgeError, e:
		print(e)
	else:
		cv2.imwrite("/home/sauranil/Desktop/Communication_Summer/drone/receive_folder/nano1%i.jpg"%i, cv2_img)
	i += 1

def callback2(msg):
	global i
	print("receiving image from nanostation 2")
	try:
		cv2_img = bridge.imgmsg_to_cv2(msg, "bgr8")
	except CvBridgeError, e:
		print(e)
	else:
		cv2.imwrite("/home/sauranil/Desktop/Communication_Summer/drone/receive_folder/nano2%i.jpg"%i, cv2_img)
	i += 1

def sender():
	global length
	info_pub.publish(length)
	for f1 in files:
		print("sending image to nanostation")
		img = cv2.imread(f1)
		image_pub.publish(bridge.cv2_to_imgmsg(img, "bgr8"))
		rate.sleep()
	flag2 = 1
	send_confirm.publish(flag2)


def info(data):
	global n
	n = data.data
	print("no of files to be received: ", data.data)

def confirm(var):
	global flag1
	flag1 += 1
	



def main():
	global count, loop, image_pub, info_pub, rate, flag, send_confirm, flag2
	rospy.init_node("drone", anonymous = True)
	info_pub = rospy.Publisher('drone_info', Int32, queue_size = 10)
	rospy.Subscriber('nano_info', Int32, info)
	rospy.Subscriber('confirmation', Int32, confirm)
	send_confirm = rospy.Publisher('send_topic', Int32, queue_size = 10)
	receive_pub = rospy.Publisher('receive_topic', Int32, queue_size = 10)
	rospy.sleep(3)
	image_pub = rospy.Publisher('image_sender', Image, queue_size = 10)
	
	rospy.Subscriber('image_receiver_nano1', Image, callback2)
	rospy.Subscriber('image_receiver_nano2', Image, callback1)

	bridge = CvBridge()

	rate = rospy.Rate(1)
	
	while not (rospy.is_shutdown()):

		inform = info_pub.get_num_connections()
		connections = image_pub.get_num_connections()
		if (inform == 1 and connections == 1 and flag == 0):
			print("receiver connected")
			sender()
			print("all files sent")
			rospy.sleep(3)
			flag = 1

		if (i == n and flag == 1 and flag1 == 1):
			receive_pub.publish(flag1)
			print("All files received")
			break
		rate.sleep()




if __name__ == '__main__':
	try:
		main()
	except rospy.ROSInterruptException:
		pass
