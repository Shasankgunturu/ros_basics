#!/usr/bin/python3
import rospy
from custom_msgs.srv import ser, serResponse

def handle_service(req):
    if req.a > req.b:
        r = True
        print("returning true")
    else:
        r = False
        print("returning false")
    return serResponse(r)

if __name__ == "__main__":
    rospy.init_node("Server_Server")
    s = rospy.Service("is_a_g_b", ser, handle_service)
    rospy.spin()
