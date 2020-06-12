# Lecture Notes 4

## For Loop
* It is one of the type of loop
* It uses __in range()__ function
* Variations of for loop
  * For Example:
    * Starts from 0, executes till `n-1` and updation by 1 each time
```
for x in range(6):
  print(x)
```
    * Starts from `a`, executes till `n-1` and updation by 1 each time
```
for x in range(2, 6):
  print(x)
```
    * Starts from `a`, executes till `n-1` and updation by `b` each time
```
for x in range(2, 30, 2):
  print(x)
```
* Program - [Program for Variations in For Loop](https://github.com/abhinavg916/ytcodehelp-python/blob/master/Lectures/Lecture%204/VariationsOfForLoop.py)

## Functions
* Python program begins from `main` function
* It is defined with the help of `def` keyword
* Functions are always called when to be used
* For Example:
  * Variable is not required if the function return void
```
def myFunc1(): # Function Definition
  print("Hi, I am Abhinav")

myFunc1() # Function Calling
```
  * It is must to store returned value from a function into a variable
```
def myFunc2(a , b): # Arguments
  return a + b

result = myFunc2(4, 3) # Parameters
print(result)
```
* Program - [Program for Function](https://github.com/abhinavg916/ytcodehelp-python/blob/master/Lectures/Lecture%204/Functions.py)

## Import and From Command
* `import` is used for importing contents of other program into the current file.
* It imports only the necessary and required contents
* `.` operator is used to access the contents(method, variables, etc)
* It helps in
  * Reducing Code Redundancy
  * Saving Time
  * Better Code Readability
* Syntax:
```
import FileName
print(FileName.MemberName)
```
* For Example:
```
import Functions
print(Functions.x)
```
* `from` is used for importing contents of other program into the current file.
* It provides the ablility to import all or selected contents
* It does not uses and does not require `.`operator to access
* To import all the content, `*` is used
* Syntax:
```
from FileNme import *
print(MemberName)
```
* For Example:
```
from Functions import *
print(x)
printHello()
result =  myFunc2(8,10)
print(result)
```
* Program - [Program for Import and From Statements](https://github.com/abhinavg916/ytcodehelp-python/blob/master/Lectures/Lecture%204/ImportAndFrom.py)
