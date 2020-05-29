if __name__ == '__main__':
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    l.reverse()
    for i in range(1,n,1):
        if(l[i]<l[i-1]):
            print(l[i])
            break
