#!/usr/bin/python3

import rospy
from custom_msgs.srv import ser

def check(a,b):
    checking_bigger_num = rospy.ServiceProxy("is_a_g_b", ser)
    q = checking_bigger_num(a, b)
    return q.s

if __name__ == "__main__":
    rospy.init_node("service_client")
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    rospy.wait_for_service("is_a_g_b")
    r = check(a,b)
    if r:
        print("yes")
    else:
        print("no")
