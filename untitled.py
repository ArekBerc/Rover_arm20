from math import *
# need to find rotational matrices to fond r unkonowns
"""x=-300
y=0
z=-400
eq1=Eq([sin(t2)*sin(t3)*cos(t1) - cos(t1)*cos(t2)*cos(t3)])
eq2=Eq([-sin(t1)])
eq3=Eq([-sin(t2)*cos(t1)*cos(t3) - sin(t3)*cos(t1)*cos(t2)])
eq4=Eq([300*sin(t2)*sin(t3)*cos(t1) - 400*sin(t2)*cos(t1) - 300*cos(t1)*cos(t2)*cos(t3) - x])
eq5=Eq([sin(t1)*sin(t2)*sin(t3) - sin(t1)*cos(t2)*cos(t3)])
eq6=Eq([cos(t1)])
eq7=Eq([-sin(t1)*sin(t2)*cos(t3) - sin(t1)*sin(t3)*cos(t2)])
eq8=Eq([-sin(t1)*sin(t2)*cos(t3) - sin(t1)*sin(t3)*cos(t2) - y])
eq9=Eq([sin(t2)*cos(t3) + sin(t3)*cos(t2)])
eq10=Eq([0])
eq11=Eq([sin(t2)*sin(t3) - cos(t2)*cos(t3)])
eq12=Eq([300*sin(t2)*cos(t3) + 300*sin(t3)*cos(t2) - 400*cos(t2) - z])

		
	

	solve((eq4,eq8,eq12),(t1,t2,t3))"""


a=300*sin(pi/2)*sin(pi/2)*cos(0) - 400*sin(pi/2)*cos(0) - 300*cos(0)*cos(pi/2)*cos(pi/2) 
b=-sin(0)*sin(pi/2)*cos(pi/2) - sin(0)*sin(pi/2)*cos(pi/2)
c=300*sin(pi/2)*cos(pi/2) + 300*sin(pi/2)*cos(pi/2) - 400*cos(pi/2)
print(a)
print(b)
print(c)