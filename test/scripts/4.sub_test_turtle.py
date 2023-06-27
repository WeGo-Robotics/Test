#!/usr/bin/env python3

import rospy
from turtlesim.msg import Pose

rospy.init_node("wego_sub_node")  # node name


def counter_CB(data):
    print(data)


rospy.Subscriber("/turtle1/pose", Pose, counter_CB)  # pub or sub
rospy.spin()
