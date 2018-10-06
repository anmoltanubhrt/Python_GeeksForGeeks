Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.

lines=input("Enter the lines you want to convert into uppercase")
nw_lines=lines.upper()
print(nw_lines)
# This is another way of doing it'
lines=[]
while True:
    s=raw_input()
    if s:
        lines.append(s.upper())
    else:
        break
for sentence in lines:
    print sentence
