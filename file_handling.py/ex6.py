import json
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p = Person('akash',21)
def show_object(p):
    if isinstance(p,Person):
        return 'name {} age {}'.format(p.name,p.age)

with open('a.json','w') as f:
    json.dump(p,f,default=show_object)

# deserialization
with open('a.json','r') as r:
    d = json.load(r)
    print(d)

