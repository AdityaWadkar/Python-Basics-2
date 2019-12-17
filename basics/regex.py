## Regex Cheatsheet
## https://www.cheatography.com/davechild/cheat-sheets/regular-expressions/
## https://www.py4e.com/lectures3/Pythonlearn-11-Regex-Handout.txt
## Video: https://www.coursera.org/learn/python-network-data/lecture/5LN6R/11-2-extracting-data

## Python Regular Expression Quick Guide
## 
## ^        Matches the beginning of a line
## $        Matches the end of the line
## .        Matches any character
## \s       Matches whitespace
## \S       Matches any non-whitespace character
## *        Repeats a character zero or more times
## *?       Repeats a character zero or more times 
##          (non-greedy)
## +        Repeats a character one or more times
## +?       Repeats a character one or more times 
##         (non-greedy)
## [aeiou]  Matches a single character in the listed set
## [^XYZ]   Matches a single character not in the listed set
## [a-z0-9] The set of characters can include a range
## (        Indicates where string extraction is to start
## )        Indicates where string extraction is to end


import re
x = 'My 2 favorute numbers are 19 and 422'
y = re.findall('[0-9]+' , x)
print(y)
print('--------------------')

#greedy matching
## matching until you find a colon, problem there is also a colon later in the string
## greedy matching takes the big thing, non greedy matching stops after the first colon
x =  'From: Using the : character'
y = re.findall('^F.+:' , x)
print('Greedy: ' , y)
print('--------------------')

#non greedy matching
y = re.findall('^F.+?:' , x)
print('Non-Greedy: ' , y)
print('--------------------')


#finding email address
x =  'From stephen.marquard@uct.ac.za Satz Jan 5 09:14:16 2008'
y = re.findall('\S+@\S+' , x)
print('Email: ' , y)
print('--------------------')

#finding email address with a from before
y = re.findall('^From \S+?@\S+' , x)
print('Email: ' , y)
print('--------------------')

#extract only the email address but not the from, but it must be there to match
y = re.findall('^From (\S+?@\S+)' , x)
print('Email: ' , y)
print('--------------------')


#extract only the domain
y = re.findall('@([^ ]*)' , x)
print('Email: ' , y)
print('--------------------')