import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from math import *

# Here (a,b) - Centre
# ra - semi major axis
# rb - Semi Minor axis

def ellipse(a,b,ra,rb):
	ra=2*ra
	rb=2*rb
	plt.figure()
	ax=plt.gca()
	ellipse=Ellipse(xy=(a,b),width=ra,height=rb,angle=0)
	ax.add_patch(ellipse)
	#ax.set_xlim([-2*ra,2*ra])
	#ax.set_ylim([-2*rb,2*rb])
	plt.axis('scaled')
	plt.show()

def manipulated_to_main(list1,list2):
	tuples_list=[]
	main_list=[]
	for i in range(len(list1)):
		tuples_list=[]
		tuples_list.append(list1[i])
		tuples_list.append(list2[i])
		main_list.append(tuples_list)
	for j in range(len(main_list)):
			main_list[j].append(1)
	return main_list

def row_mult(l1,l2):
	sum=0
	for i in range(len(l1)):
		sum=sum + l1[i]*l2[i]
	return sum
a=input()
if a=="disc":
	d=list(map(int,input().split()))
	cx=d[0]
	cy=d[1]
	r=d[2]
	r1=r
	r2=r
	ellipse(cx,cy,r1,r2)
	inp=input()
	while inp!="quit":
		if inp[0]=="S":
			inp=inp[2:]
			rs=inp.split()
			rsx=int(rs[0])
			rsy=int(rs[1])
			new_a=row_mult([r1,0],[rsx,0])
			new_b=row_mult([0,r2],[0,rsy])
			# print (" New a - ",new_a)
			# print (" New b - ",new_b)
			ellipse(cx,cy,new_a,new_b)
			print (cx,cy,new_a,new_b)
			r1=new_a
			r2=new_b
		elif inp[0]=="T":
			inp=inp[2:]
			rt=inp.split()
			rtx=int(rt[0])
			rty=int(rt[1])
			new_cx=row_mult([cx,0,1],[1,0,rtx])
			new_cy=row_mult([0,cy,1],[0,1,rtx])
			ellipse(new_cx,new_cy,r1,r2)
			print (new_cx,new_cy,r1,r2)
			cx=new_cx
			cy=new_cy
		elif inp[0]=="R":
			degree=int(inp[2:])
			theta=degree*(pi/180)
			new_cx=row_mult([cx,cy],[cos(theta),-sin(theta),0])
			new_cy=row_mult([cx,cy],[sin(theta),cos(theta),0])
			ellipse(new_cx,new_cy,r1,r2)
			print (new_cx,new_cy,r1,r2)
			cx=new_cx
			cy=new_cy
		inp=input()

if a=="polygon":
	plt.ion() # makes the plot interactive
	x=list(map(int,input().split()))
	y=list(map(int,input().split()))
	main_list=manipulated_to_main(x,y)
	x.append(x[0])
	y.append(y[0])
	plt.plot(x,y)
	b=input()
	while b!="quit":
		if b[0]=="S":
			b=b[2:]
			ls=b.split()
			sx=int(ls[0])
			sy=int(ls[1])
			manipulated_list_x_s=[]
			manipulated_list_y_s=[]
			for s in range(len(main_list)):
				c1s=row_mult(main_list[s],[sx,0,0])
				c2s=row_mult(main_list[s],[0,sy,0])
				manipulated_list_x_s.append(c1s)
				manipulated_list_y_s.append(c2s)
			print (manipulated_list_x_s,manipulated_list_y_s)
			main_list=manipulated_to_main(manipulated_list_x_s,manipulated_list_y_s)
			manipulated_list_x_s.append(manipulated_list_x_s[0])
			manipulated_list_y_s.append(manipulated_list_y_s[0])
			plt.plot(manipulated_list_x_s,manipulated_list_y_s)
		elif b[0]=="R":
			degree=int(b[2:])
			theta=degree*(pi/180)
			manipulated_list_x_r=[]
			manipulated_list_y_r=[]
			for r in range(len(main_list)):
				c1r=row_mult(main_list[r],[cos(theta),-sin(theta),0])
				c2r=row_mult(main_list[r],[sin(theta),cos(theta),0])
				manipulated_list_x_r.append(c1r)
				manipulated_list_y_r.append(c2r)
			print (manipulated_list_x_r,manipulated_list_y_r)
			main_list=manipulated_to_main(manipulated_list_x_r,manipulated_list_y_r)
			manipulated_list_x_r.append(manipulated_list_x_r[0])
			manipulated_list_y_r.append(manipulated_list_y_r[0])
			plt.plot(manipulated_list_x_r,manipulated_list_y_r)
		elif b[0]=="T":
			b=b[2:]
			lt=b.split()
			tx=int(lt[0])
			ty=int(lt[1])
			manipulated_list_x_t=[]
			manipulated_list_y_t=[]
			for t in range(len(main_list)):
				c1t=row_mult(main_list[t],[1,0,tx])
				c2t=row_mult(main_list[t],[0,1,ty])
				manipulated_list_x_t.append(c1t)
				manipulated_list_y_t.append(c2t)
			print (manipulated_list_x_t,manipulated_list_y_t)
			main_list=manipulated_to_main(manipulated_list_x_t,manipulated_list_y_t)
			manipulated_list_x_t.append(manipulated_list_x_t[0])
			manipulated_list_y_t.append(manipulated_list_y_t[0])
			plt.plot(manipulated_list_x_t,manipulated_list_y_t)
		b=input()
