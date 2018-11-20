# Communication-Relay-using-Wifi-Mesh
Communication Relay by creating a WiFi Mesh Network ( essentially making IoT Nodes) using ROS, and using that network for Data Telemetry, with Telemetry radios ( Ubiquiti Bullet, Ubiquiti Nanostation) being used as Access Points and Base stations. These are mounted on Drones (with provision for Autopilot using PixHawk modules) so as to facilitate large scale operations at remote locations, accompanied with an Android App. All of this is achieved **Without the use of an Active Internet Connection.**

# Instructions for installing ROS:
Install either ROS Kinetic / ROS Indigo, preferrably ROS Kinetic.
http://wiki.ros.org/ROSberryPi/Installing%20ROS%20Kinetic%20on%20the%20Raspberry%20Pi


# Instructions for setting up new Ubiquiti Nanostation Loco M2:
https://bit.ly/2BjKcC1
https://bit.ly/Nanostation

After following this, connect to the Designated WiFi SSID you have created, go to Edit Connections, and then set a Static IP Address, as per your choice.

# The Complete Pipeline ( How, and the order in which the files work )
1. Drone checks connection to both the Nanostations using ping command(as used using the terminal) (chk_connection.py)
2. Whichever Nano the drone gets connected to, the transfer will take place with that Nano(dronecomm1.sh)
3. Data syncing is done with the respective nano (drone1.py)
4. It will ping the other nanostation ( chk_connection1.py)
5. Data syncing is done again with that Nano(The one with which the connection is established in the upper case). (dronecomm2.sh)
6. Again it will ping the first (chk_connection2.py)



# Steps to get the System Running:
1. Open terminal ( Alt+ Ctrl + T), and type in **rosversion -d**, to check if ROS has been correctly or not.
   If the version name is shown, it means that it has been correctly installed an dis good to go.
2. Get to the directory where check **check_connection.py** is located, and type in **./check_connection.py**.
   For example, **cd Desktop/Summer\ Communications\ Project\ IP/comm_src/src/comm/src/** and then the above command.
   This would get the system going, and all the processes, as mentioned in the above Pipeline Process, will begin, and in order.
3. The files and folders that need to be in the same directory are: 
      1. check_connection.py
      2. nano2_comm.sh
      3. nanostation2.py
      4. send_folder
      5. receive_folder
4. To kill all the processes, type in **killall -9 rosmaster**

# Login details for the WiFis and the RPis & Ubiquiti Domain details

1. 1. User:ubnt
   2. Password: iiitd_ubnt
   3. Preset IP Address: 192.168.1.158



2. 1. User:ubnt
   2. Password: ubnt123
   3. IP Address: 192.168.1.160


3. 1. Raspberry Pi
   2  user: iiitd
   3. IP Address: 192.168.1.200
   4. Password: test@123


4. Access Point 1:
   1. WiFi SSID: ubiquiti_IIITD
   2. Password: ubiquiti_iiitd123


5. Access Point 2
   1. WiFi SSID: ubnt_IIITD
   2. Password: ubiquiti_iiitd123




