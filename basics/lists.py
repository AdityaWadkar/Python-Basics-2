
print("############## definite loop with for keyword")
friends = ["Joseph","Peter" , "Sally" ] 

for friend in friends :
    print("Happy New Year: " , friend)
print("Done!")



print("############## Range!")
friend = ""
for i in range(len(friends)) :
    friend = friends[i]
    print('Happy New Year:' , friend)


print("############## Append")
friends.append('Patrik')
print(friends)

print("############## Is in the list")
friends.append('Patrik')

if "Patrik" in friends :
    print("Patrik is in friends: " , friends)


print("############## Sort a list of numbers")

lotto = [32, 4, 326, 41, 63]
print(lotto)
lotto[2] = 28

print(lotto)
print("sort lotto")
lotto.sort()
print(lotto)

print("min" , min(lotto)  )
print("max" , max(lotto)  )
print("sum" , sum(lotto)  )