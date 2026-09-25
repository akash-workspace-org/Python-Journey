import pickle
class Student:
    def __init__(self,name,rollNo):
        self.name = name
        self.rollNo = rollNo

obj = Student('akash','08')
with open('studentDemu.pkl','wb') as f:
    pickle.dump(obj,f)