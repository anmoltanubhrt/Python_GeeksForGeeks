#This is the script for testing the functionalities of string

a = "This is a string"
print (a)
a = "y the way"
print (a)

# Now, we are checking the homogenous structure of the lists
l = [1,"a","string",1+2]
print (l)
print ("we are adding element 3 to the list")
l.append(3)
print (l)
print ("removing an element from the list")
l.pop()
print (l)
print ("the first element in the list is ")
print (l[1])

# Checking the functionality of the tuples in Python
tup = (1,"adfa","ad",1+2)
print (tup)

# Understanding Iterations in Python
print ("printing using the while loop")
i= 1
while (i<10):
    print (i)
    i = i + 1

print ("Printing using the for loop")
string = "Hello World"
for i in string:
    print (i)

print ("Looping over a list")
for i in l:
    print (i)

print ("Looping using the for loop and range function")
for i in range(0,4):
    print (i)
    
    
    
