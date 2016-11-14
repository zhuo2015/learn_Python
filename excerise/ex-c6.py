import os
os.chdir('c:\\Users\\john\hfpython2')

class Athlete:
    def __init__(self,a_name,a_dob,a_times=[1]):
        # the code to initialize a 'Athlete' object.
        self.name = a_name
        self.dob = a_dob
        self.times = a_times
        
