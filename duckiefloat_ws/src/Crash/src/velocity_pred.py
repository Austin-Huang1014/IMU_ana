#! /usr/bin/env python

import rospy
import numpy
from sensor_msgs.msg import Imu
from geometry_msgs.msg import Vector3

def callback(data):
    global t_last,a,b,c
    t_now = rospy.get_time()
    acc_x = data.linear_acceleration.x
    acc_y = data.linear_acceleration.y
    acc_z = data.linear_acceleration.z
    Vx = a + (acc_x)*(t_now-t_last)
    Vy = b + (acc_y)*(t_now-t_last)
    Vz = c + (acc_z)*(t_now-t_last)
    vcc = numpy.sqrt(Vx*Vx + Vy*Vy + Vz*Vz)
    V = Vector3(Vx,Vy,Vz)
    f = open('/home/arg/dockiefloat_ws/src/Crash/src/a.txt','a')
    f.writelines(str(V)+'\n'+str(vcc)+'\n')
    f.close()
    t_last = t_now


if __name__ == '__main__':
     a = 0
     b = 0
     c = 0
     rospy.init_node('velocity_ana',anonymous=True)
     rospy.Subscriber('df02/imu',Imu, callback)
     t_last = rospy.get_time()
     rospy.spin()