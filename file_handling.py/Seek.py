with open('sample1.txt','r') as f:
    print(f.read(5))
    print(f.seek(0))
    print(f.read(5))