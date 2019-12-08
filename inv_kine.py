import numpy as np
from calculations_dh import *
from Robotic_arm import *

def inv_kine(r,p,treshold=0.01,max_iter=100):

	q=r.qc
	T=f_kine(r,q)
	x=np.array([[T[0,3,3]],[T[1,3,3]],[T[2,3,3]]])
	jacob=jac(r,q)
	print(jacob)

	current_iter=1

	while True:
		current_iter = current_iter + 1
		
		delta_pos = p - x

	
		delta_angle = np.dot(np.linalg.pinv(jacob),delta_pos)

		for i in range(4):
			q[i]=q[i]+delta_angle[i]

		x,y=f_kine_ee(r,q)

		jacob=jac(r,q)



		err=np.sqrt((delta_pos[0])**2)+((delta_pos[1])**2)+((delta_pos[2])**2)
		print(err)

		if err<treshold or current_iter > max_iter:
			break


	return q,current_iter,err