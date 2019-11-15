from math import *
import numpy as np
from random import randint
from sympy import *



class robotic_arm():
	"""docstring for ClassName"""
	t0=Symbol('t0')
	t1=Symbol('t1')
	t2=Symbol('t2')
	t3=Symbol('t3')
	t4=Symbol('t4')
	t5=Symbol('t5')


# there is an option to not use a class
  	def __init__(self, param_theta, param_a, param_d, param_alpha):
		self.param_theta=[t1,(pi/2)+t2,(pi/2)+t3,t4,(pi/2)+t5,0]
		# param_a and param_d variables are guesses about the link lengths.
		self.param_a =[0,400,300,0,0,0] 
		self.param_d = [0,0,0,150,0,100]
		self.param_alpha=[-pi/2,0,pi/2,-pi/2,pi/2,0]
		
	def genT(theta, a, d, alpha):
		T =  np.array([[cos(theta), (-sin(theta)), 0, a],
    	[sin(theta)*cos(alpha), (cos(theta)*cos(alpha)), -sin(alpha), (-   d*sin(alpha))],
    	[sin(theta)*sin(alpha), cos(theta)*sin(alpha), cos(alpha), cos(alpha)*d],
    	[0, 0, 0, 1]])

		return T

	T0_1=genT(t1,0,0,-pi/2)
	T1_2=genT((pi/2)+t2,400,0,0)
	T2_3=genT((pi/2)+t3,300,0,pi/2)
	T3_4=genT(t4,0,150,-pi/2)


	T0_2=np.dot(T0_1,T1_2)
	T0_3=np.dot(T0_2,T2_3)


	print(T0_3)


	
	