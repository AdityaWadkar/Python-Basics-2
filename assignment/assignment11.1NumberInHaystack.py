# https://www.py4e.com/tools/python-data/?PHPSESSID=705c79a0d499bab9f7e30babad8b0275

# Finding Numbers in a Haystack

# In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum 
# of the numbers.

# Data Files
# We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual 
# data you need to process for the assignment.

# Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt (There are 90 values with a sum=445833)
# Actual data: http://py4e-data.dr-chuck.net/regex_sum_332119.txt (There are 100 values and the sum ends with 536)
# These links open in a new window. Make sure to save the file into the same folder as you will be writing your Python program. 
# Note: Each student will have a distinct data file for the assignment - so only use your own data file for analysis.

# Solving the problem:
# 1 The basic outline of this problem is to read the file, 
# 2 look for integers using the re.findall(), looking for a regular expression of '[0-9]+' 
# 3 and then converting the extracted strings to integers and summing up the integers.
import re
s = 0

f = open( "../files/regex_sum_332119.txt" )
for line in f:
    y = re.findall('[0-9]+' , line)
    if len(y) > 0: 
        for sNumber in y:
            iNumber = int(sNumber)
            s = s + (iNumber)
            

print("Sum" , s)