#! /usr/bin/env python

import rospy
import numpy
from sensor_msgs.msg import Imu
from geometry_msgs.msg import Vector3

def callback(data):
     global a,b,c,t2,i
     t1 = rospy.get_time()
     x = data.orientation.x
     y = data.orientation.y
     z = data.orientation.z
     X = data.linear_acceleration.x
     Y = data.linear_acceleration.y
     Z = data.linear_acceleration.z
     a = x - a
     b = y - b
     c = z - c
     dir = 0
     Dir = 0
     if(c>0):
        if((a>0)and(b>0)):
           dir = 1
        if((a<0)and(b>0)): 
           dir = 2
        if((a<0)and(b<0)):
           dir = 3
        if((a>0)and(b<0)):
           dir = 4
     if(c<0):
        if((a<0)and(b>0)):
           dir = 5
        if((a>0)and(b>0)): 
           dir = 6
        if((a>0)and(b<0)):
           dir = 7
        if((a<0)and(b<0)):
           dir = 8
     if(Z>0):
        if((X>0)and(Y>0)):
           Dir = 1
        if((X<0)and(Y>0)): 
           Dir = 2
        if((X<0)and(Y<0)):
           Dir = 3
        if((X>0)and(Y<0)):
           Dir = 4
     if(Z<0):
        if((X<0)and(Y>0)):
           Dir = 5
        if((X>0)and(Y>0)): 
           Dir = 6
        if((X>0)and(Y<0)):
           Dir = 7
        if((X<0)and(Y<0)):
           Dir = 8
     vcc = (numpy.sqrt(a*a + b*b + c*c))/(t1-t2)
     acc = numpy.sqrt(X*X + Y*Y + Z*Z)
     f = open('/home/arg/dockiefloat_ws/src/Crash/src/b.txt','a')
     f.writelines('vcc_value:' + str(vcc) + '\n' + 'dir:' + str(dir) + '\n' + 'Acc_value:'+str(acc) +'\n'+'dir'+str(Dir)+'\n'+'=========================' + str(rospy.get_time() - i) + '\n')
     f.close()
     #rospy.loginfo(str(vcc)+'\n'+str(a/(t1-t2))+'\n'+str(b/(t1-t2))+'\n'+str(c/(t1-t2))+'\n')
     t2 = t1
     a = x
     b = y
     c = z
     

if __name__ == '__main__':
     a = 0 
     b = 0
     c = 0
     rospy.init_node('velocity_dir',anonymous=True)
     t2 = rospy.get_time()
     rospy.Subscriber('df02/imu',Imu, callback)
     i = t2
     rospy.spin()
