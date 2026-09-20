with open('sample1.txt','r') as f:
    print(f.tell())
    print(f.read(5))
    print(f.tell())