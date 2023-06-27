#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32

rospy.init_node("wego_sub_node")  # node name


def counter_CB(data):
    print(data)


rospy.Subscriber("/counter", Int32, counter_CB)  # pub or sub
rospy.spin()
