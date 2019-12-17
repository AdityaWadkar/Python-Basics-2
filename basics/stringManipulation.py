helloString = "Banana"

print("#######################################################")
print("string length")
# string length

print("helloString length: " , len(helloString) )
print(helloString[0] + helloString[1] )


print("#######################################################")
print("# look up each letter - while loop version")
# look up each letter indefinite while loop

i = 0
while i < len(helloString):
    letter = helloString[i]
    print("index: " , i , letter)
    i = i + 1


print("#######################################################")
print("# look up each letter - for loop version")
# look up each letter indefinite while loop

i = 0
count = 0
for letter in helloString :
    if letter == 'a' :
        count = count + 1
    print(letter)
print("Count of letter a: " , count)


print("#######################################################")
print("# slice strings, get a substring")

s = "Monty Python"
print(s[0:5])
print(s[:5])
print(s[5:])
print(s[:])

print("#######################################################")
print("# In operator")

s = "Monty Python"
if 'Monty' in s :
    print("Found it: ", s) 