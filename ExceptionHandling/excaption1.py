try:
    f = open('sample.txt','r')
    data =  f.read()
    l = [1,2,3]
    if 3 != l:
        raise Exception('Kuch to garbar hai')
except FileNotFoundError:
    print('error')
except Exception as e:
    print(e)
else:
    print('Welcome')
finally:
    f.close()
    print('file closed: ')