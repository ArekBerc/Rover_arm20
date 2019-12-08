from math import *
import numpy as np
from random import randint
from sympy import *



class robotic_arm():
	"""docstring for ClassName"""
	t1, t2, t3, t4, t5, t6=symbols('t1 t2 t3 t4 t5 t6')


# there is an option to not use a class
  	

		
	def genT(theta, a, d, alpha):
		T =  np.array([[cos(theta), (-sin(theta)*cos(alpha)),sin(theta)*sin(alpha) , cos(theta)*a],
    	[sin(theta), (cos(theta)*cos(alpha)), -sin(alpha)*cos(theta), a*sin(theta)],
    	[0, sin(alpha), cos(alpha), d],
    	[0, 0, 0, 1]])

		return T

	"""t=[t1,t2+(pi/2),t3+(3*pi/4),t4,t5+(pi/2),t6]
	a=[0,400,0,150,0,0]
	d = [0,0,300,0,100,0]
	alpha=[3*pi/4,0,3*pi/4,pi/2,3*pi/4,0]"""
	t=[t1,(pi/2)+t2,(pi/2)+t3,t4,(pi/2)+t5,0]
	a =[0,400,300,0,0,0]
	d = [0,0,0,150,0,100]
	alpha=[-pi/2,0,pi/2,-pi/2,pi/2,0]

	T0_1=genT(t[0],a[0],d[0],alpha[0])
	T1_2=genT(t[1],a[1],d[1],alpha[1])
	T2_3=genT(t[2],a[2],d[2],alpha[2])
	T3_4=genT(t[3],a[3],d[3],alpha[3])
	T4_5=genT(t[4],a[4],d[4],alpha[4])



	T0_2=np.dot(T0_1,T1_2)
	T0_3=np.dot(T0_2,T2_3)
	T0_4=np.dot(T0_3,T3_4)
	T0_5=np.dot(T0_4,T4_5)

# we are goint to use them by two part one for the 0 to 3 (arm) and one for the 3 to 6 (gripper)

# the result that we have is different from expexted
# this algortihm replaces base coordinat system to the destination point and gives us the coordinat of base point respected to destination
# this is not a problem at all we can use negative values when we give destination point

# The equatios above gives us the unknown angle values but how 	(x y z is the destination point parameters we give to the controller)
#300*sin(t2)*sin(t3)*cos(t1) - 400*sin(t2)*cos(t1) - 300*cos(t1)*cos(t2)*cos(t3) + x 
#300*sin(t1)*sin(t2)*sin(t3) - 400*sin(t1)*sin(t2) - 300*sin(t1)*cos(t2)*cos(t3) +y
#300*sin(t2)*cos(t3) + 300*sin(t3)*cos(t2) - 400*cos(t2) +z 
