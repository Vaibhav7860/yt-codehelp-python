def solve(s):
    temp=list(s)
    temp[0]=temp[0].upper()
    for i in range (1,len(temp)):
        if temp[i-1]==" ":
            temp[i]=temp[i].upper()
    return "".join(temp)

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
s = input()
result = solve(s)
print(result)
# fptr.write(result + '\n')
# fptr.close()
