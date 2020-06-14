# Lecture Notes 10

## 2D List
* List stores data into in continous memory allocation
* Unlike normal list which stores numeric value or characters in it and is declared as
```
list = [] # Empty List
```
* 2D List - Stores list as a part of it i.e List of Lists
* It is very much helpful for storing matrix elements
* Syntax:
  * Creation
```
vairableListName = [[], []]
```
  * Taking Dynamic Input
    * for loop can also be used
```
ll = [] # Empty List
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
ll.append(a)
ll.append(b)
ll.append(c)
print(ll) # Output - [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```
* For Example:
  * Creation
```
l = [[1,2,3], [4,5,6], [7,8,9]]
for i in l:
    print(i)

# Output
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]
```
  * Dynamic Input
```
ll = []
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
ll.append(a)
ll.append(b)
ll.append(c)
print(ll) # Output - [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```
* Program - [Program for 2D List Basics](https://github.com/abhinavg916/ytcodehelp-python/blob/master/Lectures/Lecture%2010/2DListIntroduction.py)

## Recursion
* Recursion - Self Calling Functions are called as Recursive Functions
* It has two parts:
  * Base Condition - Stopping Condition for recursion
  * Recursive Expression
* Method calls are stored in Stack Memory
* It is widely used in Traversals of various Data Structures like Trees, Graphs and Algorithms like Backtracking, Dynamic Programming, etc.
* Logic Building is simpler than Iteration
* Program - [Program for Calculating Factorial of a Number using Recursion](https://github.com/abhinavg916/ytcodehelp-python/blob/master/Lectures/Lecture%2010/FactorialRecursion.py)
