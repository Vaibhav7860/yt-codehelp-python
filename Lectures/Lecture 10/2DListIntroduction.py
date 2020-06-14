# Static Input
l = [[1,2,3], [4,5,6], [7,8,9]]
for i in l:
    print(i)

# Dynamic Input
ll = []
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

ll.append(a)
ll.append(b)
ll.append(c)
print(ll)
