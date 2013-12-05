from core_plot import *
power = np.random.random(100).reshape((10,10))
mycore = Core()
mycore.addVariable(power, 'Power','W',True)
mycore.plot(0,0)
