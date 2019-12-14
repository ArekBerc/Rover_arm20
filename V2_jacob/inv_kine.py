import numpy as np
from calculations_dh import *
from Robotic_arm import *

def inv_kine(r,p,treshold=0.01,max_iter=100):

	q=r.qc
	T=f_kine(r,q)
	x=np.array([[T[0,3,3]],[T[1,3,3]],[T[2,3,3]]])
	jacob=jac(r,q)
	#print(jacob)
	#print("b")
	#print(q)
	#print("b")
	current_iter=1

	while True:
		current_iter = current_iter + 1
		print("p")
		print(p)
		print("p")
		print("x")
		print(x)
		print("x")
		delta_pos = p - x

		#print(np.linalg.pinv(jacob))
		#print(delta_pos)
		delta_angle = np.dot(np.linalg.pinv(jacob),delta_pos)
		#print("a")
		#print(delta_angle)
		#print("a")

		y,x=f_kine_ee(r,q)
		for i in range(4):
			q[i]=q[i]+delta_angle[i][0]
			if(q[i]<r.lb[i]):
				q[i]=r.lb[i]
			if(q[i]>r.ub[i]):
				q[i]=r.ub[i]


		print(np.degrees(q))
		jacob=jac(r,q)



		err=np.sqrt((delta_pos[0])**2)+((delta_pos[1])**2)+((delta_pos[2])**2)
		print(err)

		if err<treshold or current_iter > max_iter:
			break

	#print(q)
	return q,current_iter,err
