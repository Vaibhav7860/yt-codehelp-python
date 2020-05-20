def count_substring(string, sub_string):
    sumCount = 0
    for i in range (len(string)):
       if string[i:i + len(sub_string)] == sub_string:
            sumCount+=1
    return sumCount

string = input()
sub_string = input()
count = count_substring(string, sub_string)
print(count)