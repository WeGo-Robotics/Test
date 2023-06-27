#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32

rospy.init_node("wego_pub_node")  # node name
pub = rospy.Publisher("/counter", Int32, queue_size=1)  # pub or sub
count = 0  # data
rate = rospy.Rate(10)  # data publish rate
while not rospy.is_shutdown():
    count += 1
    pub.publish(count)
    rate.sleep()
