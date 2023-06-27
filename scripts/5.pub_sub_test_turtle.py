#!/usr/bin/env python3

import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from random import *

rospy.init_node("wego_node")  # node name
sub_data = Pose()
pub_data = Twist()


def counter_CB(sub_data):
    print(f"tutle_x: {sub_data.x}")
    print(f"tutle_y: {sub_data.y}")
    pub_data.linear.x = random()
    pub_data.angular.z = random() * 4 - 2
    if True:
        pass

    pub.publish(pub_data)


pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=1)  # pub or sub
rospy.Subscriber("/turtle1/pose", Pose, counter_CB)  # pub or sub
rospy.spin()
