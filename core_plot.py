import Image
import numpy as np
import ImageDraw
import ImageFont
import matplotlib.pyplot as plt
import os



class Core(object):
    def __init__(self):
        self.img_core = Image.new('RGB', (1000, 1000), 'white')
        self.draw_core = ImageDraw.Draw(self.img_core)
        self.matrices = []
        self.units = []
        self.names = []
        self.plot_color = ''
        self.font = ImageFont.truetype(os.getcwd() + '/Helvetica.ttf', 14)

    def addVariable(self, matrix, name, units, bool_color):
        self.matrices.append(matrix)
        self.units.append(units)
        self.names.append(name)
        if bool_color:
            self.plot_color = name
        
        print len(self.matrices)

    def plot(self, matrix_number, digits):
        xmax = self.matrices[0].shape[0]
        ymax = self.matrices[0].shape[1]

        xsize = 800/xmax
        ysize = 800/ymax

        self.draw_core.rectangle([20,850,20+xsize,850 + ysize], (0,0,255))




        for m in range(len(self.matrices)):
                   
            matrix = self.matrices[m]
            name = self.names[m]
            unit = self.units[m]
                
            maxval = np.max(matrix)
                       
            print matrix
                       
            for y in range(ymax):
                for x in range(xmax):
                    if m == matrix_number:
                        print "m = matrix_number and m =", m
                        
                    
                    
                    # get color for enr pins
##                    if (matrix[x,y]/maxval <= 1.0/3.0):
##                        red = 0.0
##                        green = 3.0 * matrix[x,y]/maxval
##                        blue = 1.0
##                    elif (matrix[x,y]/maxval <= 2.0/3.0):
##                        red = 3.0 * matrix[x,y]/maxval - 1.0
##                        green = 1.0
##                        blue = -3.0 * matrix[x,y]/maxval + 2.0
##                    else:
##                        red = 1.0
##                        green = -3.0 * matrix[x,y]/maxval + 3.0
##                        blue = 0.0
                    
                    # convert color to RGB triplet
                        red = int(255*matrix[x][y])
                        green = int(255*matrix[x][y])
                        blue = int(255*matrix[x][y])
                        print red
                        print green
                        print blue

                        if matrix[x,y] != 0:
                            if name == self.plot_color:
                                self.draw_core.rectangle([x*xsize,y*ysize,(x+1)*xsize,(y+1)*ysize], (red,green,blue), outline = "white")

                            if len(self.matrices) == 1:
                                self.draw_core.text([x*xsize + 3./8*xsize,y*ysize+3./8*ysize], str(matrix[x,y])[:5], (0,0,0), self.font)
                            elif len(self.matrices) == 2:
                                self.draw_core.text([x*xsize + 3./8*xsize,y*ysize+(2./8 + 3./8*m)*ysize], str(matrix[x,y])[:self.digits], (0,0,0), self.font)
                            elif len(self.matrices) == 3:
                                self.draw_core.text([x*xsize + 3./8*xsize,y*ysize+(1./8 + 2./8*m)*ysize], str(matrix[x,y])[:self.digits], (0,0,0), self.font)
                        else:
                            print "Something's bad..."
                       
            if len(self.matrices) == 1:
                self.draw_core.text([20 + 3./8*xsize,850+3./8*ysize],name, (0,0,0), self.font)
            elif len(self.matrices) == 2:
                self.draw_core.text([20 + 3./8*xsize,880+(2./8 + 3./8*m)*ysize], name, (0,0,0), self.font)
            elif len(self.matrices) == 3:
                self.draw_core.text([20 + 3./8*xsize,880+(1./8 + 2./8*m)*ysize], name, (0,0,0), self.font)
                       

                       
        self.img_core.save("core2.png")
