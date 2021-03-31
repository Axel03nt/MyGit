import numpy as np
import matplotlib.pyplot as plt

f = open("hop02.txt", mode = 'r', encoding='utf-8')
D = []
count = 1
for i in f:
	if count <= 500:
		D.append(float(i))
	count = 1 + count


a = 0.125
b = 0.25
R0 = 0
dev0 = 0
DEV = []
ERTT = []
t = []
for i in range(0,len(D)):
	sa = D[i]
	RTT = (1-a)*R0 + a*sa
	dev = (1-b)*dev0+b*abs(sa-RTT)
	DEV.append(dev)
	dev0 = dev
	R0 = RTT
	ERTT.append(RTT)
	
	t.append(ERTT[i]+4*DEV[i])
	error = (1 /len(ERTT))*(np.sum(ERTT[i] - D[i])**2)

#Gràficas de forma individual
fig1 = plt.figure("Test")
fig1.subplots_adjust(hspace = 0.5, wspace = 0.5)
ax = fig1.add_subplot(4,1,1)
ax.plot(D)
ax.set_title('ICMP')

ax = fig1.add_subplot(4,1,2)
ax.plot(ERTT)
ax.set_title('ERTT')

ax = fig1.add_subplot(4,1,3)
ax.plot(DEV)
ax.set_title('DEV')

ax = fig1.add_subplot(4,1,4)
plt.xlim(0,500)
ax.plot(t)
ax.set_title('timeout')

plt.show()

#Gràfias superpuestas
plt.plot(D, color = 'purple')
plt.plot(ERTT, color = 'red')
plt.plot(t, color = 'lightblue')
plt.xlim(0,500)
plt.legend(("ICMP", "ERTT", "TIMEOUT"), prop = {'size':10}, loc='upper right')
plt.title('Graficas superpuestas')
plt.show()






