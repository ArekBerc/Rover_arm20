from Robotic_arm import *
from std_msgs.msg import Float64
import rospy
from calculations_dh import *
from inv_kine import *
import numpy as np
from math import pi
from sensor_msgs.msg import Joy
from std_msgs.msg import Float64 as F64








def callback(data):


    xp=data.axes[1]/10



def comm():
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
        q, k, err = inv_kine(arm, np.array([[xp], [0.], [0.]]))
        arm=selfUpdater(arm,q)

        pub1.publish(qc[0])
        pub2.publish(qc[1])
        pub3.publish(qc[2])
        pub4.publish(qc[3])
        pub5.publish(qc[4])
        pub6.publish(qc[5])
#            rate.sleep()






if __name__ == '__main__':
    try:
        comm()
    except rospy.ROSInterruptException:
        pass
