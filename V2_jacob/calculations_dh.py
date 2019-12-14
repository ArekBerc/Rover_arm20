import numpy as np
from Robotic_arm import *


def f_kine(r,q):
	temp=np.ones((4,4,),dtype=float)
	T=np.zeros((4,4,4))
	for i in range(4):
		if r.typee[i]=='r':
			r.theta[i]=q[i]
		elif r.typee[i]=='p':
			r.d[i]=q[i]

	for i in range(4):
		ct=np.cos(r.theta[i]+r.offset[i])
		st=np.sin(r.theta[i]+r.offset[i])
		ca=np.cos(r.alpha[i])
		sa=np.sin(r.alpha[i])

		temp = np.dot(temp,np.array([[ct , -st*ca , st*sa , (r.a[i])*ct],
		[st , ct*ca , -ct*sa, (r.a[i])*st ],
		[0 , sa , ca , r.d[i]] ,
		[0 , 0 , 0 , 1]]))

	T[:,:,i]=temp


# CHECK THE NOTATIONS LATER !!!!!!


	for i in range(4):
		for j in range(4):
			T[j,3,i]=T[j,3,i] + r.base[j]




	return T



def f_kine_ee(r,q):

	T=f_kine(r,q)

	R=T[:3,:3,3]

	p=np.array([[T[0,3,3]],
		[T[1,3,3]],
		[T[2,3,3]]])

	return R,p


def jac(r,q):
	epsilon=0.000001
	epsilon_inv=1/epsilon

	g0,f0=f_kine_ee(r,q)
	qc0=q

	jac=np.zeros((3,4))
	for i in range(4):
		q = qc0
		q[i] = qc0[i] + epsilon
		#print(q[1])
		g1,f1=f_kine_ee(r,q)


		#print("burasi f1")
		#print(f1)

		for j in range(3):
			jac[j][i]=(f0[j]-f1[j]) * epsilon_inv

			#print("burasi f0")
			#print(f0)
	#print("this is jac")
	#print(jac)
	return jac

def selfUpdate(r, qc):
    r.qc = qc;
    r.T = f_kine(r, qc);
    r.jac = jac(r, qc);
