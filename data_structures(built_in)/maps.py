import math

def area(r):
    return math.pi * (r**2)
radii = [2, 5, 7.1, 0.3, 10]

#method 1: Direct Method
areas = []
for r in radii:
    a = area(r)
    areas.append(a)
    print("Method 1 returns each iteration:", areas)

## method 2: Using 'map' function

output = map(area, radii) #takes 2 arguements, a function and a iterable object
#print("Cant output a map", output)#output is a map not a list
areas = list(map(area, radii)) #output is a list
print("Method 2 returns all iterations:", areas)
