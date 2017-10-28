# Checking the variable type in Python
a = 3
A = 4
print (a)
print (A)

# Checking the expressions in Python

a = 2
b = 3
c = a + b
print (c)
d = a*b
print (d)

# Conditions in Python
a = 3
b = 9
if b%a == 0:
    print ("b is divisible by a")
elif b + 1 == 10:
    print ("Increment in b produces 10")
else:
    print ("You are in else statement")

# Function for checking the divisibility
# Notice the indentation after function declaration
# and if else statement

def checkDivisibility(a,b):
    if a%b == 0:
        print ("a is divisible by b")
    else:
        print (" a is not divisible by b")

# Driver program to check the above function
checkDivisibility(4,2)

# With this the script ends
