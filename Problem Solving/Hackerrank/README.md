# Things learnt during Problem Solving from Hackerrank

## Basiscs
* Type Conversion (`d = float(a/b)`)
* __strip()__ - Strip during input (`n = int(input().strip())`)

## Functions
* __end=" "__ - Continuous Output Formatting (` print(x+1, end= "")`)

## Strings
* String slicing with iteration
  ```
  for i in range (len(string)):
    string[i:i + len(sub_string)]
  ```
* __any()__ - Evaluation with iteration (`any([char.isalnum() for char in s]))`)
* Alignment (or Justified) Methods
  * __ljust()__ - Left Alignment (`str.ljust(width, [fillchar])`)
  * __rjust()__ - Right Alignment (`str.rjust(width, [fillchar])`)
  * __center()__ - Center Aligment (`str.center(width, [fillchar])`)

## Lists
* __split()__ - It splits the input based on the space and stores in the variables. (`a, b = temp.split()`)
* To represent the __last element in the list__, it is accessed by -1 index. (`l.pop(-1)`)
