from Robotic_arm import *
from std_msgs.msg import Float64
import rospy
from calculations_dh import *
from inv_kine import *
import numpy as np
from math import pi
from sensor_msgs.msg import Joy
from std_msgs.msg import Float64 as F64

qc = np.array([0.0, 0.0, 0.0, 0.0,0.0,0.0])
T = np.array([0.0, 0.0, 0.0, 0.0,0.0,0.0])
ub = np.array([pi / 2, pi / 2, pi / 2, pi / 2, pi / 2, pi / 2])
lb = np.array([-pi / 2, -pi / 2, -pi / 2, -pi / 2, -pi / 2, -pi / 2])
theta = np.array([0.0, 0.0, 0.0, 0.0,0.0,0.0])
alpha = np.array([pi/2, 0.0, pi/2, pi/2,pi/2,0.0])
offset = np.array([0.0, pi/2, -pi/2, 0.0,pi/2,-pi/2])
d = np.array([1.0, 0.0, 0.0, 10.0,0.0,15.0])
a = np.array([0.0, 30.0, 40.0, 0.0,0.0,0.0])
typee = np.array(['r', 'r', 'r', 'r','r','r'])
base = np.array([[0.0], [0.0], [0.0], [0.0],[0.0],[0.0]])
arm = Robotic_arm(base, theta, d, a, alpha, offset, qc, typee, jac, T, ub, lb)






def callback(data):

    global arm
    xp=data.axes[1]/10
    q, k, err = inv_kine(arm, np.array([[xp], [0.], [0.]]))
    arm=selfUpdater(arm,q)
    for i in range(6):
        a = F64()
        a.data = q[i]
        arm.pubme.append(a)

def comm():


    rospy.init_node('Rover_arm20', anonymous=True)
    rospy.Subscriber("/joy", Joy, callback)
    pub1 = rospy.Publisher('/rover_arm_eksen1_joint_position_controller/command', F64, queue_size=1)
    pub2 = rospy.Publisher('/rover_arm_eksen2_joint_position_controller/command', F64, queue_size=1)
    pub3 = rospy.Publisher('/rover_arm_eksen3_joint_position_controller/command', F64, queue_size=1)
    pub4 = rospy.Publisher('/rover_arm_eksen4_joint_position_controller/command', F64, queue_size=1)
    pub5 = rospy.Publisher('/rover_arm_eksen5_joint_position_controller/command', F64, queue_size=1)
    pub6 = rospy.Publisher('/rover_arm_eksen6_joint_position_controller/command', F64, queue_size=1)

#        rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        pub1.publish(arm.pubme[0])
        pub2.publish(arm.pubme[1])
        pub3.publish(arm.pubme[2])
        pub4.publish(arm.pubme[3])
        pub5.publish(arm.pubme[4])
        pub6.publish(arm.pubme[5])
#            rate.sleep()






if __name__ == '__main__':
    try:
        comm()
    except rospy.ROSInterruptException:
        pass
