import json
L = [1,2,3,4,7]
with open('sample3.json','w') as f:
    json.dump(L,f)

with open('sample3.txt','r') as r:
    d = json.load(r)
    print(tuple(d))