#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

rospy.init_node("wego_pub_node")  # node name
pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=1)  # pub or sub
rate = rospy.Rate(10)  # data publish rate
data = Twist()

while not rospy.is_shutdown():
    data.angular.z = 1
    pub.publish(data)
    rate.sleep()
