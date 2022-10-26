# HOMEWORK PROMPT NEVER STATED WHAT LIBRARYS WE CAN/CANNOT USE
# THEREFOR I AM NOT USING scipy.interpolate.griddata FOR INTERPOLATION
# AND I AM USING pandas TO REPRESENT THE TABLES

import pandas as pd

saturated = pd.read_csv("sat_water_table.txt", sep='\t', lineterminator='\n')
superheated = pd.read_csv("superheated_water_table.txt", sep='\t', lineterminator='\n') 
superheated.rename(columns = {'Pressure\r':'Pressure'}, inplace = True)

# Be careful on the units between the input ones and those given in the txt files!!! 
# TEMP IS GIVEN IN degC ON BOTH TABLES
# ENTROPY IS GIVEN IN kJ/(Kg K) ON BOTH TABLES
# ENTHALPY IS GIVEN IN kJ/Kg ON BOTH TABLES
# PRESSURE IS GIVEN IN bar ON SATURATED TABLE
# PRESSURE IS GIVEN IN kPa ON SUPERHEATED TABLE

def interpolate(property2, value1, region="Saturated"):

    index1 = None # LOWER VALUE
    index2 = None # HIGHER VALUE

    pressure = saturated['Pressure']
    
    for i in pressure:
        if (value1 >= (i * 100)): # MULTIPLY BY 100 TO CONVERT bar to kPa
            index1 = pressure.values.tolist().index(i)
    index2 = index1 + 1

    x = value1
    if region == 'Saturated':
        x1 = saturated["Pressure"][index1] * 100 # MULTIPLY BY 100 TO CONVERT bar to kPa
        x2 = saturated["Pressure"][index2] * 100 # MULTIPLY BY 100 TO CONVERT bar to kPa
        y1 = saturated[property2][index1]
        y2 = saturated[property2][index2]
    if region == "Superheated":
        x1 = superheated["Temp"][index1] * 100 # MULTIPLY BY 100 TO CONVERT bar to kPa
        x2 = superheated["Temp"][index2] * 100 # MULTIPLY BY 100 TO CONVERT bar to kPa
        y1 = superheated[property2][index1]
        y2 = superheated[property2][index2]

    y = y1 + ((y2 - y1) * ((x - x1) / (x2 - x1)))
    return y

class SteamState: 
 
    def __init__(self, pressure, name): 
        self.p = pressure   # pressure - kPa 
        self.x = None       # quality (a value between 0 and 1) 
        self.T = None       # temperature - degrees C 
        self.v = None       # specific volume - m^3 / kg 
        self.h = None       # enthalpy - kJ/kg 
        self.s = None       # entropy - kJ / (kg * K) 
        self.region = None  # 'superheated' or 'saturated' 
        self.name = name    # a useful identifier from user-defined string 

    def determineRegion(self):

        if self.x != None: 
            self.region = 'Saturated'

        elif self.T != None:
            if self.T  <= interpolate("Temp", self.p):
                self.region = 'Saturated'
            else:
                self.region = 'Superheated'

        elif self.v != None:
            if self.v  <= interpolate("vg", self.p):
                self.region = 'Saturated'
            else:
                self.region = 'Superheated'

        elif self.h != None:
            if self.h  <= interpolate("hg", self.p):
                self.region = 'Saturated'
            else:
                self.region = 'Superheated'

        elif self.s != None:
            if self.s  <= interpolate("sg", self.p):
                self.region = 'Saturated'
            else:
                self.region = 'Superheated'
    
    def calcQuality(self):
        if self.h != None:
            hf = interpolate("hf", self.p, self.region)
            hg = interpolate("hg", self.p, self.region)
            x = (self.h - hf) / (hg - hf)
        elif self.s != None:
            sf = interpolate("sf", self.p, self.region)
            sg = interpolate("sg", self.p, self.region)
            x = (self.s - sf) / (sg - sf)
        elif self.v != None:
            vf = interpolate("vf", self.v, self.region)
            vg = interpolate("vg", self.v, self.region)
            x = (self.v - vf) / (vg - vf)
        return x   

    def calcTemp(self):
        temp = interpolate("Temp", self.p, self.region)
        return temp
    
    def calcEntalpy(self):
        if self.region == "Saturated":
            hf = interpolate("hf", self.p, self.region)
            hg = interpolate("hg", self.p, self.region)
            h = hf + self.x * (hg - hf)
        else:
            h = interpolate("hg", self.p, self.region)
        return h

    def calcEntropy(self):
        if self.region == "Saturated":
            sf = interpolate("sf", self.p, self.region)
            sg = interpolate("sg", self.p, self.region)
            s = sf + self.x * (sg - sf)
        else:
            s = interpolate("sg", self.p, self.region)
        return s

    def calcSpecificVolume(self):
        if self.region == "Saturated":
            vf = interpolate("vf", self.p, self.region)
            vg = interpolate("vg", self.p, self.region)
            v = vf + self.x * (vg - vf)
        else:
            v = None
        return v

    def calc(self):

        self.determineRegion()

        if self.region == "Saturated" and self.x is None:
            self.x = self.calcQuality()

        if self.T is None:
            self.T = self.calcTemp()

        if self.h is None:
            self.h = self.calcEntalpy()

        if self.s is None:
            self.s = self.calcEntropy()

        if self.v is None:
            self.v = self.calcSpecificVolume()

    def printt(self):
        if self.name != None:
            print(f'Name: {self.name}')
        if self.region != None: 
            print(f'Region: {self.region}')
        if self.T != None:
            print(f'Temperature: T = {self.T:.1f} degrees C')
        if self.p != None:
            print(f'Pressure: P = {self.p:.2f} kPa')
        if self.h != None:
            print(f'Enthalpy: h = {self.h:.2f} kJ/kg')
        if self.s != None:
            print(f'Entropy: s = {self.s:.4f} kJ/(kg K)')
        if self.v != None:
            print(f'Specific Volume: v = {self.v:.6f} m^3/kg')
        if self.x != None:
            print(f'Quality in Saturation Region: x = {self.x:.4f}')
        print()
