"""
'''Write a program that accepts a sentence and
 calculate the number of letters and digits.
'''

sentence = raw_input("Enter a sentence") # This statement records the input the user has given
d={"DIGITS":0,"LETTERS":0} # Here, we are intializing a dictionary. The dictionary has two variables, digits and letters to store the numbers
for c in sentence:
    if c.isdigit():
        d["DIGITS"]+=1
    elif c.isalpha():
        d["LETTERS"]+=1
    else:
        pass
print("The letters are"+str(d["LETTERS"]))
print("The digits are"+str(d["DIGITS"]))
