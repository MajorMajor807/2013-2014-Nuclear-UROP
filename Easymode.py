from core_plot import *
power = np.random.random(100).reshape((10,10))
mycore = Core()
mycore.addVariable(power,'Power','W',True)
Temperature = np.random.random(100).reshape((10,10))
mycore.addVariable(Temperature,'Temp','K',False)
difference = []
for y in range(ymax):
    for x in range(xmax):
        difference[x][y] = power[x][y] - Temperature[x][y]
        print "Difference is ", difference[x][y]
mycore.plot(0,4)
