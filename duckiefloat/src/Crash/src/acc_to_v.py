#! /usr/bin/env python

import rospy
import numpy
from sensor_msgs.msg import Imu
from geometry_msgs.msg import Vector3

def callback(data):
     global Vx,Vy,Vz,t1
     x = data.linear_acceleration.x
     y = data.linear_acceleration.y
     z = data.linear_acceleration.z
     t2 = rospy.get_time()
     T = t2 - t1
     t1 = t2
     d = 0
     Vx = Vx + (T*x)
     Vy = Vy + (T*y)
     Vz = Vz + (T*z)
     d = Dir(Vx,Vy,Vz)
     V_value = numpy.sqrt(Vx*Vx + Vy*Vy + Vz*Vz)
     V = Vector3(Vx,Vy,Vz)
     pub = rospy.Publisher('Vcc',Vector3, queue_size=10)
     rate = rospy.Rate(10)
     pub.publish(V)
     #rospy.loginfo(d)
     rospy.loginfo(V)

def Dir(X,Y,Z):
     if(Z>0):
        if((X>0)and(Y>0)):
           D = 1
        if((X<0)and(Y>0)): 
           D = 2
        if((X<0)and(Y<0)):
           D = 3
        if((X>0)and(Y<0)):
           D = 4
     if(Z<0):
        if((X<0)and(Y>0)):
           D = 5
        if((X>0)and(Y>0)): 
           D = 6
        if((X>0)and(Y<0)):
           D = 7
        if((X<0)and(Y<0)):
           D = 8
     return D
     

if __name__ == '__main__':
     Vx = 0
     Vy = 0
     Vz = 0
     rospy.init_node('velocity_ana',anonymous=True)
     t1 = rospy.get_time()
     rospy.Subscriber('df02/imu',Imu, callback)
     rospy.spin()
