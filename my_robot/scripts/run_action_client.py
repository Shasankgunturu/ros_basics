#!/usr/bin/python3

import rospy
import actionlib
from custom_msgs.msg import acAction, acFeedback,acResult, acGoal

def ac_client():
    client = actionlib.SimpleActionClient("ac_action",  acAction)
    client.wait_for_server()
    goal = acGoal()
    goal.targer = 10
    client.send_goal()
    client.wait_for_result()
   
       # Prints out the result of executing the action
    return client.get_result() 
    

if __name__ == "__main__":
    rospy.init_node("action_client")
