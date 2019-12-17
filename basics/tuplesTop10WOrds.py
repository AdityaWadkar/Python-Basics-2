f = open('../files/romeo.txt')
counts = dict()

# count words using a dictionary
for line in f:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1 
        

# move the words to a list
lst = list()
for key, val in counts.items():
    newtup = (val , key)
    lst.append(newtup)

# sort the list
lst = sorted(lst, reverse= True)


# print out the top 10 words
for v,k in lst[:10]:
    print( k , v)