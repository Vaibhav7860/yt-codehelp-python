import matplotlib.pyplot as plt

# plt.ion()

x = [1, -1, -1, 1, 1] # List of X-coordinates of points
y = [1 ,1 ,-1, -1, 1] # List of Y-coordinates of points

# x=list(map(int,input().split()))
# y=list(map(int,input().split()))

# x.append(x[0])
# y.append(y[0])

plt.plot(x,y) # To plot the points
plt.show() # To display the plotted points