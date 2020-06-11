# Lecture Notes 8

## Dictionaries: Basic Operation
* It is meant for storing associated __key and values pairs__ together
* Elements stored in dictionaries are called as __Tuples__
* With the help of key, respective value can be accessed
* Dictionaries are __un-ordered__ whereas list are ordered which means ordered can be accessed by the help of indices. Thus, dictionaries have no indexing. It returns error as "KeyError" upon accessing following way:
```
stuMarks = {'Abhinav': 90,'Babbar': 100,'Rahul':80,'Ajay':95}
print(stuMarks[2]) # Key Error because 2 is treated as key, not as index in dictionaries
```
* Key can only be integer or a string
* Values can be of any type (decimal, string, integer, list, etc)
```
new = {'Abhinav':[100, 90,80], 'Babbar':[100,95,80]}
print(new) # Output - {'Abhinav': [100, 90, 80], 'Babbar': [100, 95, 80]}
```
* Syntax:
  * Creation
```
variableName = { }
variableName = {'Abhinav': 90,'Babbar': 100,'Rahul':80,'Ajay':95}
```
  * Printing
```
variableName = {'Abhinav': 90,'Babbar': 100,'Rahul':80,'Ajay':95}
print(variableName)
```
  * Accessing all keys
    * __keys()__ is used
```
variableName.keys()
```
  * Accessing all values
    * __values()__ is used
```
variableName.values()
```
  * Length Calculation
    * __len()__ is used  
```
len(listVariableName)
``` 
* For Example:
  * Creation
```
teachers = { } # Empty Dictionary
stuMarks = {'Abhinav': 90,'Babbar': 100,'Rahul':80,'Ajay':95} # Here, Abhinav is key and 90 is value.
```
  * Printing
```
stuMarks = {'Abhinav': 90,'Babbar': 100,'Rahul':80,'Ajay':95}
print(stuMarks) # Output - {'Abhinav': 90, 'Babbar': 100, 'Rahul': 80, 'Ajay': 95}
```
  * Accessing all keys
```
stuMarks = {'Abhinav': 90,'Babbar': 100,'Rahul':80,'Ajay':95}
l = stuMarks.keys()
print(l) # Output - dict_keys(['Abhinav', 'Babbar', 'Rahul', 'Ajay'])
```
  * Accessing all values
```
stuMarks = {'Abhinav': 90,'Babbar': 100,'Rahul':80,'Ajay':95}
l = stuMarks.values()
print(l) # Output - dict_values([90, 100, 80, 95])
```
  * Length of a dictionary
```
stuMarks = {'Abhinav': 90,'Babbar': 100,'Rahul':80,'Ajay':95}
print(len(stuMarks)) # Output - 4
```
* Program - [Program for Dictionary Access](https://github.com/abhinavg916/ytcodehelp-python/blob/master/Lectures/Lecture%208/DictionaryAccess.py)

## Dictionaries: Insertion
* When new key does not matches with the existing in the dictionary then it gets inserted otherwise value of the respective key is updated
* Syntax:
```
variableName[New Key] = New Value
```
* For Example:
```
stuMarks = {'Abhinav': 90,'Babbar': 100,'Rahul':80,'Ajay':95}
stuMarks['Don'] = 99
print(stuMarks) # Output - {'Abhinav': 90, 'Babbar': 100, 'Rahul': 80, 'Ajay': 95, 'Don': 99}
```
* Program - [Program for Dictionary Insertion](https://github.com/abhinavg916/ytcodehelp-python/blob/master/Lectures/Lecture%208/DictionaryInsertion.py)

## Dictionaries: Updation
* Key is used to target the updation
* Syntax:
```
variableName[Key] = New Value
```
* For Example:
  * Selective Updation
```
stuMarks = {'Abhinav': 90,'Babbar': 100,'Rahul':80,'Ajay':95}
stuMarks['Abhinav'] = 100
print(stuMarks) # Output - {'Abhinav': 100, 'Babbar': 100, 'Rahul': 80, 'Ajay': 95}
```
  * Collective Updation
    * __for loop__ and __in__ is used 
```
stuMarks = {'Abhinav': 90,'Babbar': 100,'Rahul':80,'Ajay':95}
for i in stuMarks:
    print(i, stuMarks[i])
# Output:
Abhinav 100
Babbar 100
Rahul 80
Ajay 95
```
    * Keys are being stored in `i` during the loop due to which `stuMarks[i]` is treated as value
* Program - [Program for Dictionary Updation](https://github.com/abhinavg916/ytcodehelp-python/blob/master/Lectures/Lecture%208/DictionaryUpdation.py)

## Dictionaries: Deletion
* Deletion happens in form of pair which means selective key or value is not deleted
* __del__ keyword is used
* Key is used to target for deletion of the pair
* Syntax:
```
del variableName[Key]
```
* For Example:
```
stuMarks = {'Abhinav': 90,'Babbar': 100,'Rahul':80,'Ajay':95}
del stuMarks['Abhinav']
print(stuMarks) # Output - {'Babbar': 100, 'Rahul': 80, 'Ajay': 95}
```
* Program - [Program for Dictionary Deletion](https://github.com/abhinavg916/ytcodehelp-python/blob/master/Lectures/Lecture%208/DictionaryDeletion.py)

## Dictionaries: Searching
* __Searching value from a corresponding key__
  * Key is used to target and corresponding value is returned
  * Syntax:
```
variableName[KeyToFind]
```
  * For Example:
```
stuMarks = {'Abhinav': 90,'Babbar': 100,'Rahul':80,'Ajay':95}
l = stuMarks['Abhinav']
print(l) # Output - 90
```
* __Searching for key-value pairs__
  * __in__ keyword is used
  * Syntax:
```
if(Key in variableName):
  print("Message")
else:
  print("Message")
```
  * For Example:
```
stuMarks = {'Abhinav': 90,'Babbar': 100,'Rahul':80,'Ajay':95}
if('Abhinav' in stuMarks):
  print("Present") # Output - Present
else:
  print("Absent")
```
* Program - [Program for Dictionary Searching](https://github.com/abhinavg916/ytcodehelp-python/blob/master/Lectures/Lecture%208/DictionarySearch.py)
