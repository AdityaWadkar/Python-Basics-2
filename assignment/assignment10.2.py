# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the hours for each hour, print out the hours, sorted by hour as shown below.

# read file
name = "../files/mbox-short.txt"
f = open(name)

hours = dict()

# extract time
for line in f:
    if line.startswith('From '):
        words = line.strip().split() 
        time = words[5].split(':')
        hour = time[0]
        
        # add hours to a dictionary and count up
        hours[hour] = hours.get(hour, 0) + 1
        
# get a sorted list of dictionary items and print it out
for k,v in sorted(hours.items()) :
        print( k, v)