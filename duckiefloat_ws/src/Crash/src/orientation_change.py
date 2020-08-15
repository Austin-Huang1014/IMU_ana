#! /usr/bin/env python

import rospy
import numpy
from sensor_msgs.msg import Imu
from geometry_msgs.msg import Vector3

def callback(data):
     x = data.orientation.x
     y = data.orientation.y
     z = data.orientation.z
     global a,b,c
     a = x - a
     b = y - b
     c = z - c
     V = Vector3(a,b,c)
     pub = rospy.Publisher('change_orientation',Vector3, queue_size=10)
     rate = rospy.Rate(10)
     pub.publish(V)
     rospy.loginfo(V)
     a = x
     b = y
     c = z
     

if __name__ == '__main__':
     a = 0 
     b = 0
     c = 0
     rospy.init_node('orientation_do',anonymous=True)
     rospy.Subscriber('df02/imu',Imu, callback)
     rospy.spin()
