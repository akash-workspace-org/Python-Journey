import pickle
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p = Person('akash',21)
with open('pDemo.pkl','wb') as f:
    pickle.dump(p,f)

with open('pDemo.pkl','rb') as r:
    d = pickle.load(r)
    print(d)