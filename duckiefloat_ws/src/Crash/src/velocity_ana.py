#! /usr/bin/env python

import rospy
import numpy
from sensor_msgs.msg import Imu
from geometry_msgs.msg import Vector3

def callback(data):
     global a,b,c,t2,count_1,count_2,count_3,count_4,count_5
     t1 = rospy.get_time()
     x = data.orientation.x
     y = data.orientation.y
     z = data.orientation.z
     a = x - a
     b = y - b
     c = z - c
     #V = Vector3(a/(t1-t2),b/(t1-t2),c/(t1-t2))
     vcc = (numpy.sqrt(a*a + b*b + c*c))/(t1-t2)
     if vcc<0.01:
          count_1 += 1
     if (vcc<0.1)and(vcc>0.01):
          count_2 += 1
     if (vcc>0.1)and(vcc<1):
          count_3 += 1
     if (vcc>1)and(vcc<10):
          count_4 += 1
     if vcc>50:
          count_5 += 1
     #pub = rospy.Publisher('Vcc',Vector3, queue_size=10)
     #rate = rospy.Rate(10)
     #pub.publish(V)
     rospy.loginfo(str(count_1)+'\n'+str(count_2)+'\n'+str(count_3)+'\n'+str(count_4)+'\n'+str(count_5)+'\n')
     t2 = t1
     a = x
     b = y
     c = z
     

if __name__ == '__main__':
     a = 0 
     b = 0
     c = 0
     count_1 = 0
     count_2 = 0
     count_3 = 0
     count_4 = 0
     count_5 = 0
     rospy.init_node('velocity_ana',anonymous=True)
     t2 = rospy.get_time()
     rospy.Subscriber('df02/imu',Imu, callback)
     rospy.spin()