#indefinite loop with while keyword
n = 5
while n > 0 :
    print(n)
    n = n -1

print(n)
print("Blastoff!")



#definite loop with for keyword
for i in [5, 4, 3, 2 , 1 , 0 ] :
    print(i)
print("Blastoff!")


#definite loop with for keyword
friends = ["Joseph","Peter" , "Sally" ] 

for friend in friends :
    print("Happy New Year: " , friend)
print("Done!")


# Example, what is the largest number
# https://www.coursera.org/learn/python/lecture/EyMRk/5-3-finding-the-largest-value

numbers = [9, 41, 12, 3, 74 ,14 ] 
tempLargest = 0

for number in numbers :
    if number > tempLargest:
        tempLargest = number
print("Largest Number: ", tempLargest)