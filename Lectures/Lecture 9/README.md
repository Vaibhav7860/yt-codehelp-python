# Lecture Notes 9

## Computer Graphics Basics
* A fundamental aspect of ‘Computer Graphics’, this concept is crucial in:
    * Object modelling
    * Object visualization
    * Creating projections of objects
* Objects in a scene are a collection of points
* Objects have a location, orientation, and size
* Correspond to transformations:
    * Translation(T) <=> location
    * Rotation (R) <=> orientation
    * Scaling (S) <=> size

## MatPlot Library: Basics
* It is a python library used for plotting geometry of polygons
* To use, first download and install the library through command line (or terminal)
```
pip install matplotlib
```
* For Example:
```
import matplotlib.pyplot as plt
x = [1, -1, -1, 1, 1] # List of X-Coordinates of points
y = [1 ,1 ,-1, -1, 1] # List of Y-Coordinates of points
plt.plot(x,y) # To plot the points
plt.show() # To display the plotted points
```
* For a Polygon, Start and End points must be same. In other words, the last point in the list of coordinates (X and Y) must be the very first point so that polygon is closed
* Program - [Program for Plotting Square](https://github.com/abhinavg916/ytcodehelp-python/blob/master/Lectures/Lecture%209/PlotingSquare.py)
![Output](https://github.com/abhinavg916/ytcodehelp-python/blob/master/Lectures/Lecture%209/Square.JPG)
* Problem Statement - [Assignment](https://github.com/abhinavg916/ytcodehelp-python/blob/master/Lectures/Lecture%209/Assignment.pdf)
* Program - [Assignment Program](https://github.com/abhinavg916/ytcodehelp-python/blob/master/Lectures/Lecture%209/AssignmentProgram.py)
