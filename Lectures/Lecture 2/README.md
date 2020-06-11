# Lecture Notes 2

__Error Handling__
* How to resolve error, copy the complete error and paste in the Google.
* StackOverflow is one of the best website for error resolution.

## Variables
* Stores the data into it
* It declared before use. Declaration means reserving space in the memory pool.
* Variable Initialisation means putting value in it.
* Value is assignment from right to left, not true vice-versa.
* For Example:
  * r = 10 -> This means 10 is stored in the variable 'r'
  *  10 = r -> This means r is to stored in the constant value 10, which is incorrect.
  * Similarly, r = r + 2 -> Value of r is increment by value of 2.
    * As a mathematical expression, it is not valid because r - r = 2 => 0 != 2
* Program - [Program to Calculate the Area of Circle](https://github.com/abhinavg916/ytcodehelp-python/blob/master/Lectures/Lecture%202/CircleArea.py)
```
  r = 10
  area = 3.14 * r * r
  print(area)
```
* `" "` quotes are used only for printing Strings
  * print("Hello")
  * print("area")  //Wrong because here area is a variable not a string
* Types of Variables
  * Integers - -ve to +ve numbers
  * Float - Decimal numbers
  * String - Sequence of Characters

## Taking Console Inputs
* input() is used to take dynamic input from console.
* Python treats input taken from console as Strings. So, it is must to type cast for numeric values.
* For Example:
```
  r = int(input())
  area = 3.14 * r * r
  print(area)
```
* `#` is used for Commenting code in Python. Shortcut key is __CTRL + /__
* To print the output in single line, `end = " "` is used
```
print("Hello", end= " ")
print("World")
```
  Output : Hello World

## Basics of Strings
```
  str1 = "Abhinav"
  str2 = "Dhiman"
  print(str1 + " " + str2)
```
* Program - [Program to Display User Full Name](https://github.com/abhinavg916/ytcodehelp-python/blob/master/Lectures/Lecture%202/UserName.py)
