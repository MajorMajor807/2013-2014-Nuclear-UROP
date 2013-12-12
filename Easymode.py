from core_plot import *
power = np.random.random(100).reshape((10,10))
mycore = Core()
mycore.addVariable(power,'Power','W',True)
Temperature = np.random.random(100).reshape((10,10))
mycore.addVariable(Temperature,'Temp','K',False)
difference = []

for x in range(mycore.matrices[0].shape[0]):
    templist = []
    for y in range(mycore.matrices[0].shape[1]):
        templist.append(power[x][y] - Temperature[x][y])
    difference.append(templist)
mycore.addVariable(difference, 'Diff','D',False)
mycore.plot(0,5,.25)
