#! /usr/bin/env python

import rospy
import numpy
from sensor_msgs.msg import Imu
from std_msgs.msg import Float64
from geometry_msgs.msg import Vector3

def callback(data):
     global a,b,c,A,B,C,aa,bb,cc,i,k,t2
     t1 = rospy.get_time()
     if k == 0:
      f = open('/home/austin/IMU_ana/duckiefloat/src/Crash/src/test.txt','a')
      f.writelines(str(t1 - i) + '\n')
      f.close()
      k += 1
     ax = data.angular_velocity.x
     ay = data.angular_velocity.y
     az = data.angular_velocity.z
     A = ax - A
     B = ay - b
     C = az - C
     #---------------------------------
     X = data.linear_acceleration.x
     Y = data.linear_acceleration.y
     Z = data.linear_acceleration.z
     acc = numpy.sqrt(X*X + Y*Y + Z*Z)
     aa = X - aa
     bb = Y - bb
     cc = Z - cc
     #---------------------------------
     ox = data.orientation.x
     oy = data.orientation.y
     oz = data.orientation.z
     a = ox - a
     b = oy - b
     c = oz - c
     #---------------------------------
     vcc = (numpy.sqrt(a*a + b*b + c*c))/(t1-t2)
     acc = numpy.sqrt(X*X + Y*Y + Z*Z)
     V1 = Vector3(ax,ay,az)
     V2 = Vector3(X,Y,Z)
     V3 = Vector3(ox,oy,oz)
     C1 = Vector3(A,B,C)
     C2 = Vector3(aa,bb,cc)
     C3 = Vector3(a,b,c)
     #pub = rospy.Publisher('Acc',Float64, queue_size=10)
     #rate = rospy.Rate(10)
     #pub.publish(acc)
     if (ax>=0.5) or (ay>=0.5) or(az>=0.5) or(vcc>=50) or (acc>=40):
       f = open('/home/arg/dockiefloat_ws/src/Crash/src/crash.txt','a')
       f.writelines(str(V1)+'\n'+'\n'+str(C1)+'\n'+'\n'+str(V2)+'\n'+str(C2)+'\n'+str(acc)+'\n'+'\n'+str(V3)+'\n'+'\n'+str(C3)+'\n'+'\n'+str(vcc)+'\n'+'=============='+str(t1 - i)+'\n')
       f.close()
     t2 = t1
     A = ax
     B = ay
     C = az
     aa = X
     bb = Y
     cc = Z
     a = ox
     b = oy
     c = oz
     #rospy.loginfo()



def DIR(a,b,c):
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
     return dir

if __name__ == '__main__':
     k = 0
     a = 0 
     b = 0
     c = 0
     A = 0
     B = 0 
     C = 0
     aa = 0
     bb = 0 
     cc = 0
     rospy.init_node('linear_acc_get',anonymous=True)
     t2 = rospy.get_time()
     rospy.Subscriber('df02/imu',Imu, callback)
     i = t2
     rospy.spin()
