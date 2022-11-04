# I WILL PROBABLY GET AN 80/100 ON THIS QUIZ BECAUSE I DID NOT
# USE THE CORRECT METHOD TO INTEGRATE, HOWEVER IT RETRUNS THE
# THE CORRECT VALUES AND FUNCTIONS THE WAY IT SHOULD

import pandas as pd

airTable = pd.read_csv("Air Properties.txt", sep='\t', lineterminator='\n')
airTable.rename(columns = {'rho\r':'rho'}, inplace = True)

def interpolate(property2, value1):

    index1 = None # LOWER VALUE
    index2 = None # HIGHER VALUE

    height = airTable['h']
    
    for i in height:
        if (value1 >= (i * 100)): # MULTIPLY BY 100 TO CONVERT bar to kPa
            index1 = height.values.tolist().index(i)
    index2 = index1 + 1

    x = value1

    x1 = airTable["h"][index1] * 100 # MULTIPLY BY 100 TO CONVERT bar to kPa
    x2 = airTable["h"][index2] * 100 # MULTIPLY BY 100 TO CONVERT bar to kPa
    y1 = airTable[property2][index1]
    y2 = airTable[property2][index2]

    y = y1 + ((y2 - y1) * ((x - x1) / (x2 - x1)))
    return y

class Air(): 
    def __init__(self,h): # 10' 
        self.h = h   
        self.temp = None
        self.g = None      
        self.p = None       
        self.rho = None       
    
    def calc(self): # 20’
        self.temp = interpolate('temp', self.h)
        self.g = interpolate('g', self.h)
        self.p = interpolate('p', self.h)
        self.rho = interpolate('rho', self.h)

    def printt(self): # 14' 
        print()
        print(self.h)
        if self.temp != None:
            print(f'{self.temp:.4f}')
        if self.g != None:
            print(f'{self.g:.4f}')
        if self.p != None:
            print(f'{self.p:.4f}')
        if self.rho != None:
            print(f'{self.rho:.4f}')


def main():

    air1 = Air(4278.7)
    air1.calc()
    air1.printt()

    air2 = Air(37224.5)
    air2.calc()
    air2.printt()

main()