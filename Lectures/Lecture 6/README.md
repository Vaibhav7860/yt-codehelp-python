# Lecture Notes 6

## List: Basic Operations
* It is a collection which stores number of variables in continuous memory space
* It follows indices to access the elements
* Syntax:
* Creation
```
variableName = []
variableName = [1,2,3]

```

* Accessing Elements
```
variableName[index]
```

* Length Calculation
    * __len()__ is used
```
len(listVariableName)
```

* For Example:
* Creation
```
l1 = [] # Empty List
l2 = [1,2,3] # List with elements in it
print(l1)
print(l2)
```

* Accessing
```
l = [1,2,3]
print(l[1]) # Output = 2
```

* Length of a list
```
l = [1,2,3]
print(len(l)) # Output = 3
```

* Program - [Program for Length of List](https://github.com/abhinavg916/ytcodehelp-python/blob/master/Lectures/Lecture%206/ListLength.py)
* __Taking Dynamic Inputs__
```
l = []
n = 5
for i in range(n):
    a = int(input())
    l.append(a)

print(l)
```
* Program - [Program for Dynamic Input](https://github.com/abhinavg916/ytcodehelp-python/blob/master/Lectures/Lecture%206/ListDynamicInput.py)
* __Sum of Elements__ in a list
* __sum()__ is used
* It calculates the sum of all elements in a list
* Syntax:
```
sum(listVariableName)
```
* For Example:
```
l = [1,2,3,4,5,6,6,6,6,6]
print(sum(l)) # Output = 45
```
* Program - [Program to Find Total Sum in List](https://github.com/abhinavg916/ytcodehelp-python/blob/master/Lectures/Lecture%206/ListSum.py)

## List: Slicing
* List follows the same principle as of strings
* For Example:
```
l = [1,2,3,4,5,6]
x = [1:4]
print(x) # Output = [2,3,4]
```
* Program - [Program for Slicing in List](https://github.com/abhinavg916/ytcodehelp-python/blob/master/Lectures/Lecture%206/ListSlicing.py)

## List: Insertion
* __append()__
    * It adds the element in the end of the list
    * Syntax:
```
listVariableName.append(element)
```
    * For Example:
```
l = [1,2,3,4,5,6]
l.append(7)
print(l) # Output = [1, 2, 3, 4, 5, 6, 7]
```
* __extend()__
    * It adds another list to a list
    * Ut adds in the end of the list
    * Syntax is similar to append()
    * For Example:
```
l = [1,2,3,4,5,6]
b= [20,10]
l.extend(b)
print(l) # Output = [1, 2, 3, 4, 5, 6, 20, 10]
```
* __insert()__
    * It adds the element at the desired index and shifts rest of the elements
    * Syntax:
```
variableName.insert(targetIndex, element)
```
    * For Example:
```
l = [1,2,3,4,5,6]
l.insert(0, 0)
print(l) # Output = [0, 1, 2, 3, 4, 5, 6]
```
* Program - [Program for Input or Insertion in List](https://github.com/abhinavg916/ytcodehelp-python/blob/master/Lectures/Lecture%206/ListInsertion.py)

## List: Sorting
* __sort()__ is used
    * Syntax:
```
variableName.sort()
```
* For Example:
```
l = [1,2,3,4,5,6]
x = l[1:4]
print(x) # Output = [2, 3, 5, 6]
```
* Program - [Program to Sort a List](https://github.com/abhinavg916/ytcodehelp-python/blob/master/Lectures/Lecture%206/ListSorting.py)

## List: Deletion
* __pop()__ is used
* It deletes the element based on the index provided
* Syntax
```
variableName.pop(index)
```
* For Example:
```
l = [5,2,3,6]
l.pop(3)
print(l) # Output = [5, 2, 3]
```
* Program - [Program to Delete Element from a List](https://github.com/abhinavg916/ytcodehelp-python/blob/master/Lectures/Lecture%206/ListDeletion.py)

## List: Count
* It counts the occurances of an element in the list
* __count()__ is used
* Syntax:
```
variableName.count(element)
```
* For Example:
```
l = [1,2,3,4,5,6,6,6,6,6]
print(l.count(6)) # Output = 5
```
* Program - [Program to Count the Occurrences of a Element in List](https://github.com/abhinavg916/ytcodehelp-python/blob/master/Lectures/Lecture%206/ListCount.py)
