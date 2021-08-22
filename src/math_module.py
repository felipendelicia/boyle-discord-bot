def graph_quadratic_function(a, b=0, c=0, vx=0, x1=None, x2=None):
	import os
	from matplotlib import pyplot
	import os
	current_path = os.path.dirname(os.path.abspath(__file__))
	print(current_path)

	def f1(x):
   		return a*(x**2) + b*x + c

	x = range(-1000, 1000)
	pyplot.plot(x, [f1(i) for i in x])

	pyplot.axhline(0, color="black")
	pyplot.axvline(0, color="black")

	if x1==None and x2==None: pyplot.xlim(vx-50, vx+50)
	elif x2==None: pyplot.xlim(-100, +100)
	else: pyplot.xlim(x1-100, x2+100)

	pyplot.ylim(-100, 100)

	pyplot.savefig(f"{current_path}\output.png")
	pyplot.clf()

def quadratic_function(a, b, c):
	a = float(a)
	b = float(b)
	c = float(c)

	import math

	discriminating = (b**2)-4*a*c

	if discriminating > 0:
		x1 = (-b+math.sqrt((b**2)-4*a*c))/(2*a)
		x2 = (-b-math.sqrt((b**2)-4*a*c))/(2*a)
		graph_quadratic_function(a,b,c,((x1+x2)/2),x1,x2)
		return f"Discriminante = {discriminating}\n\nRaiz 1 = {x1}\nRaiz 2 = {x2}"

	elif discriminating == 0:
		graph_quadratic_function(a,b,c,0,0,None)
		return f"Discriminante = {discriminating}\n\nPor lo tanto, tiene una unica raiz:\nRaiz = 0"

	else:
		graph_quadratic_function(a,b,c,((-b)/(2*a)),None,None)
		return f"Discriminante = {discriminating}\n\nNo tiene raices!"
