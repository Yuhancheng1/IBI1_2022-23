class triathlon: #class definition
    name = ""  #The following six sentences are all defining basic attributes
    location = ""
    swim_times = 0
    cycle_times = 0
    run_times = 0
    total_times = 0
    def __init__(self,n,l,s,c,r,t): #Define the method of construction
        self.name = n
        self.location = l
        self.swim_times = s
        self.cycle_times = c
        self.run_times = r
        self.total_times = t
    def show(self): #Define output method show
        print("my name is %s, my competiton took place in %s, I swam for %d times, cycled for %d times and ran for %d times, I totaly do %d times in triathlon." %(self.name,self.location,self.swim_times,self.cycle_times,self.run_times,self.total_times))
p = triathlon ("Saul_Goodman","Los_Angles",4,6,5,15) #Reference the class and instantiate it into p, which includes various information about this person
p.show() #use the show() to out put the result
