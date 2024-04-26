#!/usr/bin/python3

import rospy
from custom_msgs.msg import mess
import random
if __name__ == "__main__":
    rospy.init_node("custom_message_tester")
    p = rospy.Publisher("/custom_msg/talk", mess, queue_size=10)
    r = rospy.Rate(10)
    while not rospy.is_shutdown():
        m = mess()
        m.a = random.randint(0, 100)
        p.publish(m)
        r.sleep()