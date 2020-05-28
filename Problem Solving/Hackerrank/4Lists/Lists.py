def InsertInList(x, p, q):
    l.insert(p,q)

if __name__ == '__main__':
    N = int(input())
l = []
for i in range(N):
    x = input()
    if(x.find("insert")>=0):
        temp = x[7:]
        a, b = temp.split()
        p = int(a)
        q = int(b)
        InsertInList(l, p, q)

    elif(x.find("print")>=0):
        print(l)

    elif(x.find("remove")>=0):
        temp = x[7:]
        temp = int(temp)
        l.remove(temp)

    elif(x.find("append")>=0):
        temp = x[7:]
        temp = int(temp)
        l.append(temp)

    elif(x.find("sort")>=0):
        l.sort()

    elif(x.find("pop")>=0):
        l.pop(-1)

    elif(x.find("reverse")>=0):
        l.reverse()
