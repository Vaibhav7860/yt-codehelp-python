# Lecture Notes 5
### Date: 15-May-2020

## Strings: Introduction
* Strings are combination of characters
* It denoted inside   `" "`
* For Example: 
  ```
  x = "Learning Strings"
  ```
* Strings are indexed from 0 to n-1
* Program - [Program to find the indices of string](https://github.com/abhinavg916/ytcodehelp-python/blob/master/Lectures/Lecture5/StringIndices.py)
* __len()__ method is used to find the length of the string
* Syntax:
  ```
  __len(strigVariable)__
  ```
* For Example  
  ```
  x = "Learning Strings"
  print(len(x)) #Output = 16
  ```
* Program - [Program to find the length of string](https://github.com/abhinavg916/ytcodehelp-python/blob/master/Lectures/Lecture5/StringLength.py)
* Accessing index out of the range of string index results in __Index Out of Range error__

## Strings: Basic Operations
* To __loop__ a string
  * For Example:
    ```
    a = "Hi Hi Hi Abhinav"
    for c in a: #It takes characters from a and puts in C till null characters is found and stops
        print(c)
    ```
* To __Upper Case__ letters in a string
  * __upper()__ is used
  * Syntax:
    ```
    stringVariable.upper()
    ```
  * For Example:
    ```
    a = "Hi Hi Hi Abhinav"
    print(a.upper())
  ```
* To __Lower Case__ letters in a string
  * __lower()__ is used
  * Syntax:
    ```
    stringVariable.lower()
    ```
  * For Example:
    ```
    a = "Hi Hi Hi Abhinav"
    print(a.lower())
    ```

## String: Slicing
* Slicing means part or sub string of a string
* Syntax:
  ```
  s = x[beginIndex:endIndex]
  ```
* It gets the characters till provided __endIndex-1__
* For Example:
  * Accessing characters from index  `a` to `b`, where a is startIndex and b is endIndex
    ```
    x = "Learning Strings"
    s = x[1:5]
    print(s) #Output = earn
    
    ```
   * Accessing characters till end index `b` 
      ```
      x = "Learning Strings"
      s = x[:5]
      print(s) #Output = Learn
      ```
   * Accessing character from starting index `a`
     ```
      x = "Learning Strings"
      s = x[1:]
      print(s) #Output = earning Strings
      ```
* Program - [Program to find substring of a string using Slicing](https://github.com/abhinavg916/ytcodehelp-python/blob/master/Lectures/Lecture5/StringSlicing.py)

## String: Count
* __count()__ function counts the number of occurances a string has appeared in other string
* If no string is found then 0 is returned
* Syntax:
  ```
  stringA.count(stringB)
  ```
* For Example:
  ```
  a = "Hi Hi Hi Abhinav"
  b = "Hi"
  count = a.count(b)
  print(count)
  ```
* Program - [Program to count the occurences in a string]()

## String: Find
* __find()__ function returns the starting index of a string present in another string
* If no string is found then -1 is returned
* Syntax:
  ```
  stringA.find(stringB)
  ```
* For Example:
  ```
  a = "Hi Hi Hi Abhinav"
  b = "Hi"
  count = a.find(b) #Output = 0
  print(count)
  ```
* Program - [Program to slice a string from desired strin then find index]() - It is also called as Cropping
* Program - [Program to display YES/NO for string]()
* Above, program is correct but Python has another keyword called as __`in`__
* For Example:
  ```
  a = "Learning Strings"
  b = "Strings"
  if(b in a):
    print("Yes")
  else:
    print("No")
  ```

## String: Replace
* It accepts two arguements, one is character as input which to be replaced and the other character for to be replaced with in a string 
* __replace()__ function is used and returns the updated string
* Syntax:
  ``` 
  stringA.replace(" ", " ")
  ```
* For Example:
  ```
  a = "Hi Hi Hi Abhinav"
  a = a.replace(" ", "")
  print(a) #Output = HiHiHiAbhinav
  ```
* Program - [Program for String replacement]()
