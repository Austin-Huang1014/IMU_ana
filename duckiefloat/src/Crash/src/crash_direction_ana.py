#! /usr/bin/env python

import rospy
import numpy
import time
from sensor_msgs.msg import Imu
from std_msgs.msg import Float64
from geometry_msgs.msg import Vector3

def callback(data):
     global r1,r2,c,V2,i
     x = data.linear_acceleration.x
     y = data.linear_acceleration.y
     z = data.linear_acceleration.z
     V1 = Vector3(x,y,z)
     if(z>0):
        if((x>0)and(y>0)):
           r1 = 1
        if((x<0)and(y>0)): 
           r1 = 2
        if((x<0)and(y<0)):
           r1 = 3
        if((x>0)and(y<0)):
           r1 = 4
     if(z<0):
        if((x<0)and(y>0)):
           r1 = 5
        if((x>0)and(y>0)): 
           r1 = 6
        if((x>0)and(y<0)):
           r1 = 7
        if((x<0)and(y<0)):
           r1 = 8
     if(r1 + r2) == 9:
        c = 1
        f = open('/home/arg/dockiefloat_ws/src/Crash/src/crash.txt','a')
        f.writelines('V1:' + '\n' + str(V1) + '\n' + '------------' + str(rospy.get_time() - i) + '\n')
        f.writelines('V2:' + '\n' + str(V2) + '\n' + '===================' + '\n')
        f.close()
        rospy.loginfo(c)
     else:
        c = 0
        rospy.loginfo(c)
     r2 = r1
     V2 = V1
     pub = rospy.Publisher('crash_dir',Float64, queue_size=10)
     rate = rospy.Rate(10)
     pub.publish(c)
     
     

if __name__ == '__main__':
     r1 = 0 
     r2 = 0
     c = 0
     V2 = Vector3(0,0,0)
     rospy.init_node('crash_dir',anonymous=True)
     rospy.Subscriber('df02/imu',Imu, callback)
     i = rospy.get_time()
     rospy.spin()