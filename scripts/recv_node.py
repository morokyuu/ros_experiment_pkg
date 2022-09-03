# -*- coding: utf-8 -*-

import rospy
from sensor_msgs.msg import Image
from std_msgs.msg import Int32MultiArray
from std_msgs.msg import String
from std_srvs.srv import Empty


class Agent:
    def __init__(self):
        self.arry_sub = rospy.Subscriber('arry_cmd', Int32MultiArray, self.ArryCallback)
        self.cmd_sub = rospy.Subscriber('agent_cmd', String, self.CmdCallback)
        self.cmd = ""

    def ArryCallback(self,data):
        print data
        print data.data
        print data.data[2]

    def CmdCallback(self,data):
        print data
        self.cmd = data.data

    def run(self):
        if self.cmd == 'run':
            print "running"
        elif self.cmd == 'stop':
            print "stopping"
        pass

if __name__ == "__main__":
    rospy.init_node('recv_node', anonymous=False)
    agent = Agent()
    print "hello"

    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        agent.run()
        rate.sleep()

