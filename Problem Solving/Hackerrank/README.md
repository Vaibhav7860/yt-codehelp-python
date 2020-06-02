# Hackerrank Problem Sets
## Python Proficiency
* Introduction
* Basic Data Types
* Strings
* Sets
* Math
* Itertools
* Collections
* Date and Time
* Errors and Exceptions
* Classes
* Built-Ins
* Python Functionals
* Regex and Parsing
* XML
* Closures and Decorators
* Numpy
* Debugging

## Things Learnt
### Basics
* Type Conversion (`d = float(a/b)`)
* __strip()__ - Strip during input (`n = int(input().strip())`)

### Functions
* __end=" "__ - Continuous Output Formatting (` print(x+1, end= "")`)

### Strings
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
* __join()__ - It joins the list elements (`"".join(l)`)
* __textwrap.fill(str, width)__ - It wraps the text based on the width (`textwrap.fill(string, max_width)`)


### Lists
* __split()__ - It splits the input based on the space and stores in the variables. (`a, b = temp.split()`)
* To represent the __last element in the list__, it is accessed by -1 index. (`l.pop(-1)`)
* In Python 3, __map__ returns an iterable object of type map, and __not a subscriptible list__, which would allow us to write map[i]. To force a list result, we can type cast to list. (`l = list(map(int, input().split()))`)
* List Comprehension way
