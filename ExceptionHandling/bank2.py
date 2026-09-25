import pickle
from bank import Bank
try:
    f = open('bank.pkl','rb')
    data = pickle.load(f)
except Exception as e:
    print(e)
else:
    print(data.balance)