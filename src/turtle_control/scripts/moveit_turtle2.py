#!/usr/bin/env python
import rospy 
from geometry_msgs.msg import Twist

def mover_tortuga():
    rospy.init_node('mover_tortuga', anonymous=True)
    pub = rospy.Publisher('/turtle2/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(2)  # 2 Hz
    
    cmd = Twist()
    cmd.linear.x = 1.0    # velocidad hacia adelante
    
    cmd.angular.z = 0.5   # velocidad de giro

    while not rospy.is_shutdown():
        pub.publish(cmd)
        rate.sleep()

def mover_tortuga_adelante():
    rospy.init_node('mover_tortuga', anonymous=True)
    pub = rospy.Publisher('/turtle2/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(2)  # 2 Hz
    time = 0

    cmd = Twist()
    cmd.linear.x = 1.0    # velocidad hacia adelante
    

    while time <= 2:
        pub.publish(cmd)
        rate.sleep()
        time = time + 1


def girar_tortuga():
    rospy.init_node('mover_tortuga', anonymous=True)
    pub = rospy.Publisher('/turtle2/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(2)  # 2 Hz
    time = 0

    cmd = Twist()
    
    cmd.linear.x = 1.0
    cmd.angular.z = 0.8   # velocidad de giro

    while time <=4:
        pub.publish(cmd)
        rate.sleep()
        time = time + 1

if __name__ == '__main__':
    try:
        while not rospy.is_shutdown():
            mover_tortuga_adelante()
            girar_tortuga()
        

    except rospy.ROSInterruptException:
        pass
