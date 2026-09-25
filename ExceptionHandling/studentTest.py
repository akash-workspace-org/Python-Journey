import pickle
with open('studentDemu.pkl','rb') as f:
    obj = pickle.load(f)
    print(obj.name,'',obj.rollNo)