import json
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p = Person('akash',21)
def show_object(p):
    if isinstance(p,Person):
        return {'name':p.name,'age':p.age}

with open('b.json','w') as f:
    json.dump(p,f,default=show_object)

