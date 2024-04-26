#!/usr/bin/python3
import rospy
from custom_msgs.msg import acAction, acFeedback,acResult 
import actionlib

class acServer(object):
    _feedback = acFeedback()
    _result = acResult()
    def __init__(self):
        self.server = actionlib.SimpleActionServer("ac_action", acAction, self.execute, False)
        self.server.start()
    def execute(self, goal):
        r = rospy.rate(10)
        for i in range(goal.targer):
            print("testing: ", i)
            self._feedback.status = True
            self.server.publish_feedback(self._feedback)
            r.sleep()
        self._result.b = 32
        self.server.set_succeeded(self._result)
    
if __name__ == "__main__":
    rospy.init_node("action_server")
    server = acServer()
    rospy.spin()

