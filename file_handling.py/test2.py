with open('sample3.txt','w') as f:
    f.write('Hello')
    f.seek(0)
    f.write('X')