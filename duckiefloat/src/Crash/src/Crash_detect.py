#! /usr/bin/env python

import rospy
import numpy
from sensor_msgs.msg import Imu
from std_msgs.msg import Float64
from geometry_msgs.msg import Vector3

class detect(object):
  def __init__(self):
     self.node_name = rospy.get_name()
     self.t2 = rospy.get_time()
     self.i = self.t2
     self.k = 0
     self.ang = Vector3(0, 0, 0)
     self.acc = Vector3(0, 0, 0)
     self.ori = Vector3(0, 0, 0)
     self.temp_1 = None
     self.temp_2 = None
     self.temp_3 = None
     self.temp_ang = None
     self.temp_acc = None
     self.temp_ori = None
     self.t1 = rospy.get_time()
     rospy.loginfo("[%s] Initializing " % (self.node_name))
     rospy.Subscriber('df02/imu',Imu, self.ana)

  def ana(self, data):
     self.t1 = rospy.get_time()
     #---------------------------------
     self.temp_1 = Vector3(data.angular_velocity.x, data.angular_velocity.y, data.angular_velocity.z)
     #self.ang = Vector3(self.temp_1(0) - self.ang(0),self.temp_1(1) - self.ang(1),self.temp_1(2) - self.ang(2))
     self.ang.x = self.temp_1.x - self.ang.x
     self.ang.y = self.temp_1.y - self.ang.y
     self.ang.z = self.temp_1.z - self.ang.z
     self.temp_ang = self.ang
     self.ang = self.temp_1
     #---------------------------------
     self.temp_2 = Vector3(data.linear_acceleration.x, data.linear_acceleration.y, data.linear_acceleration.z)
     #self.acc = Vector3(self.temp_2(0) - self.acc(0),self.temp_2(1) - self.acc(1),self.temp_2(2) - self.acc(2))
     self.acc.x = self.temp_2.x - self.acc.x
     self.acc.y = self.temp_2.y - self.acc.y
     self.acc.z = self.temp_2.z - self.acc.z
     self.temp_acc = self.acc
     self.acc = self.temp_2
     Acc = numpy.sqrt(self.temp_2.x*self.temp_2.x + self.temp_2.y*self.temp_2.y + self.temp_2.z*self.temp_2.z)
     #---------------------------------
     self.temp_3 = Vector3(data.orientation.x, data.orientation.y, data.orientation.z)
     #self.ori = Vector3(self.temp_3(0) - self.ori(0),self.temp_3(1) - self.ori(1),self.temp_3(2) - self.ori(2))
     self.ori.x = self.temp_3.x - self.ori.x
     self.ori.y = self.temp_3.y - self.ori.y
     self.ori.z = self.temp_3.z - self.ori.z
     self.temp_ori = self.ori
     Ori = (numpy.sqrt(self.ori.x*self.ori.x + self.ori.y*self.ori.y + self.ori.z*self.ori.z))/(self.t1-self.t2)
     self.ori = self.temp_3
     #---------------------------------

     if (self.temp_1.x>=0.5) or (self.temp_1.y>=0.5) or(self.temp_1.z>=0.5) or(Ori>=50) or (Acc>=40):
       f = open('/home/austin/IMU_ana/duckiefloat/src/Crash/src/test.txt','a')
       f.writelines(str(self.temp_1)+'\n'+'\n'+str(self.temp_ang)+'\n'+'\n'+str(self.temp_2)+'\n'+'\n'+str(self.temp_acc)+'\n'+'\n'+str(Acc)+'\n'+'\n'+str(self.temp_3)+'\n'+'\n'+str(self.temp_ori)+'\n'+'\n'+str(Ori)+'\n'+'=============='+str(self.t1 - self.i)+'\n')
       f.close()
     self.t2 = self.t1





if __name__ == '__main__':
     rospy.init_node('ana',anonymous=True)
     ana = detect()
     rospy.spin()