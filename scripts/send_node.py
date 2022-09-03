# -*- coding: utf-8 -*-

import rospy
from sensor_msgs.msg import Image
from std_msgs.msg import Int32MultiArray
from std_srvs.srv import Empty
from std_msgs.msg import String
import random

class Controller:
    def __init__(self):
        self.arry_pub = rospy.Publisher('arry_cmd', Int32MultiArray, queue_size=10)
        self.cmd_pub = rospy.Publisher('agent_cmd', String, queue_size=10)

    def execute(self):
        cmd = [1,2,3]
        nanka_cmd = Int32MultiArray(data=cmd)
        self.arry_pub.publish(nanka_cmd)

        txt = ["run","stop"]
        txt = random.choice(txt)
        self.cmd_pub.publish(txt)



if __name__ == "__main__":
    rospy.init_node('send_node', anonymous=False)
    controller = Controller()
    print "hello"

    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        controller.execute()
        rate.sleep()
