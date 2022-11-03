from SteamState import SteamState 
 
def main(): 
    inlet = SteamState(8000, 'Turbine Inlet') 
    inlet.x = 0.5 # 50 percent quality 
    inlet.calc() 
    inlet.printt() 
 
    outlet = SteamState(80, 'Turbine Exit') 
    outlet.s = inlet.s # use the entropy from the inlet 
    outlet.calc() 
    outlet.printt() 
 
    another = SteamState(8000, 'SteamState 3') 
    another.h = 2100 # is this saturated or superheated? 
    another.calc() 
    another.printt() 
 
    yetanother = SteamState(9000, 'SteamState 4') 
    yetanother.h = 4050 # is this saturated or superheated? 
    yetanother.calc() 
    yetanother.printt() 
 
    final1 = SteamState(8000, 'SteamState 5') 
    final1.T = 700 # this is almost certainly superheated 
    final1.calc() 
    final1.printt() 
 
if __name__ == '__main__': 
    main()