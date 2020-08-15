#! /usr/bin/env python

import rospy
import numpy
from sensor_msgs.msg import Imu
from std_msgs.msg import Float64

def callback(data):
     global count1,count2,count3,count4,count5,count6,i,a,b,c
     t1 = rospy.get_time()
     x = data.orientation.x
     y = data.orientation.y
     z = data.orientation.z
     a = x - a
     b = y - b
     c = z - c
     #acc = numpy.sqrt(x*x + y*y + z*z)
     count(c)
     #pub = rospy.Publisher('Acc',Float64, queue_size=10)
     #rate = rospy.Rate(10)
     #pub.publish(acc)
     #f = open('/home/arg/dockiefloat_ws/src/Crash/src/Vcc_dir.txt','a')
     #if acc>30:
       # f.writelines('Acc_value:'+str(acc)+'\n'+'dir:'+str(DIR(x,y,z))+'\n'+'//////////////////////'+str(rospy.get_time() - i) + '\n'+ '\n')
     #else:
        #f.writelines('Acc_value:'+str(acc)+'\n'+'dir:'+str(DIR(x,y,z))+'\n'+'============'+str(rospy.get_time() - i) + '\n'+ '\n')
     #f.close()
     rospy.loginfo('\n'+str(count1)+'\n'+str(count2)+'\n'+str(count3)+'\n'+str(count4)+'\n'+str(count5)+'\n')
     i = t1
     a = x
     b = y
     c = z



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

def count(a):
     global count1,count2,count3,count4,count5,count6
     a = abs(a)
     if a<0.001:
        count1 += 1
     if (a>0.001)and(a<0.01):
        count2 += 1
     if (a>0.01)and(a<0.1):
        count3 += 1
     if (a>0.1)and(a<1):
        count4 += 1
     #if (a>40)and(a<50):
        #count5 += 1
     if a>1:
        count5 += 1

if __name__ == '__main__':
     count1 = 0
     count2 = 0
     count3 = 0
     count4 = 0
     count5 = 0
     count6 = 0
     a = 0
     b = 0
     c = 0
     rospy.init_node('linear_acc_get',anonymous=True)
     i = rospy.get_time()
     rospy.Subscriber('df02/imu',Imu, callback)
     rospy.spin()
     
