import pickle
class Bank:
    def __init__(self,balance):
        self.balance = balance

    def withdraw(self,amount):
        if amount < 0:
            raise Exception('Negative amount: ')
        elif self.balance < amount:
            raise Exception('Gareeb itna balance nai hai: ')
        else:
            self.balance = self.balance-amount
            print('withdraw succeessful: ')

obj = Bank(10000)
try:
    obj.withdraw(9000)
except Exception as e:
    print(e)
else:
    f = open('Data2.pkl','wb')
    pickle.dump(obj,f)
finally:
    f.close()