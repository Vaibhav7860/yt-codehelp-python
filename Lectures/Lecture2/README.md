# Lecture Notes 2
### Date: 09-May-2020

__Error Handling__
* How to resolve error, copy the complete error and paste in the Google.
* StackOverflow is one of the best website for error resolution.

__Variables__
* Stores the data into it
* It declared before use. Decalaration means reserving space in the memory ppol.
* Variable Initialisation means putting value in it.
* Value is assignment from right to left, not true vice-versa.
* For Example: 
  * r = 10 -> This means 10 is stored in the variable 'r'
  *  10 = r -> This means r is to stored in the constant value 10, which is incorrect.
  * Similarly,  r = r + 2 -> Value of r is increment by value of 2. 
    * As a mathematical expression, it is not valid because r - r = 2 => 0 != 2
* Program 2: [Program to calculate the area of circle](https://github.com/abhinavg916/ytcodehelp-python/blob/master/Lectures/Lecture2/2CircleArea.py)
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

__Taking Console Inputs__
* input() is used to take dynamic input from console.
* Python treats input taken from console as Strings. So, it is must to type cast for numeric values.
* For Example:
```
  r = int(input())
  area = 3.14 * r * r
  print(area)
```
* `#` is used for Commenting code in Python. Shortcut key is __CTRL + /__

__Strings__
```
  str1 = "Abhinav"
  str2 = "Dhiman"
  print(str1 + " " + str2)
```
* Program 3 : [Program to display user full name](https://github.com/abhinavg916/ytcodehelp-python/blob/master/Lectures/Lecture2/3UserName.py)




  
