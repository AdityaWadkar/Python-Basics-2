# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
# After the dictionary is produced, the program reads through the dictionary using a maximum loop 
# to find the most prolific committer.


sender = dict()

f = open( "../files/mbox-short.txt" )

i = 0

for line in f:
    if line.startswith('From '):
        words = line.strip().split() 
        email = words[1]
        #print(email)
        sender[email] = sender.get(email, 0) + 1
        i = i + 1
        
maxV = 0
maxK = ""

for k,v in sender.items():
    #print( k, v);
    if v > maxV:
        maxV = v
        maxK = k

print(maxK , sender[maxK])

