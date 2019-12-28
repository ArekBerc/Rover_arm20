
class Robotic_arm:
	def __init__(self,base,theta,d,a,alpha,offset,qc,typee,jac,T,ub,lb):
		self.base=base
		self.theta=theta
		self.d=d
		self.a=a
		self.alpha=alpha
		self.offset=offset
		self.qc=qc
		self.typee=typee
		self.jac={0}
		self.T=T
		self.ub=ub
		self.lb=lb
		self.pubme=[]
