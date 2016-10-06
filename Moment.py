import math
from matplotlib import pyplot as plt
def calc(eq, x):
	return eval(eq)

def Density(x):
	return (7.935/6371000.0)*(6371000.0-x)**1.54


def EarthI(R, n, eq):
	R = float(R)
	I = 0
	yL = []
	dL = []
	Disk = 0
	for y in range(int(R*n)):
		Disk = 0
		for x in range(int(n*math.sqrt(R**2-(y/n)**2))):
			C = 2*math.pi*x/n
			Ring = (C*Density(math.sqrt(x**2+y**2)/n))*(x**2+y**2)/(n**2)
			Disk += Ring/n
		I += Disk/n
		dL.append(Disk/n)
		yL.append(y)
		print '%f , %f' %(y, Disk)
	plt.plot(yL, dL)
	#plt.show()
	return 2*I

def EarthM(R, n, eq):
	R = float(R)
	M = 0
	yL = []
	dL = []
	Disk = 0
	for y in range(int(R*n)):
		Disk = 0
		for x in range(int(n*math.sqrt(R**2-(y/n)**2))):
			C = 2*math.pi*x/n
			Ring = (C*Density(math.sqrt(x**2+y**2)/n))
			Disk += Ring/n
		M += Disk/n
		dL.append(Disk/n)
		yL.append(y)
		print '%f , %f' %(y, Disk)
	plt.plot(yL, dL)
	return 2*M

func = '(7.935/6371000.0)*(6371000.0-x)**1.54'
print EarthI(6371000.0, 0.0001, func)