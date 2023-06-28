
import rospy
from std_msgs.msg import String
from datetime import datetime
import logging

logger = logging.getLogger('__name__')
fh = logging.FileHandler("/catkin_ws/log/ros.log")
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s", "%m/%d/%Y %H:%M:%S")
fh.setFormatter(formatter)
logger.setLevel(logging.DEBUG)
logger.addHandler(fh)

def is_error(msg):
    return msg.lower().find("error") >= 0

def log(msg):
    if is_error(msg):
        rospy.logerr(msg)
        logger.error(msg)
    else:
        rospy.loginfo(msg)
        logger.info(msg)
    

def listener_callback(data):
    msg = data.data
    log(msg)

def listen_and_log():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('received_data', String, listener_callback)
    rospy.spin()

if __name__ == '__main__':
    listen_and_log()
