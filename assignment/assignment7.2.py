# 7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.
# https://www.coursera.org/learn/python-data/gradedLti/IlVLg/assignment-7-2

#fname = input('Enter the file name: ')
fname = "mbox-short.txt"
tSum = 0
i = 0


try:
    fhand = open('../files/' + fname)
except:
    print('File could not be opend:' , fname)

try:
    for line in fhand:
        line = line.rstrip()
        if line.startswith("X-DSPAM-Confidence:") :
            #print(line)
            fValStartPos = line.find(":") + 2
            fVal = line[fValStartPos:]
            fVal = float(fVal)
            tSum = tSum + fVal
            i = i + 1

            #print("pos" , fValStartPos)
            #print("fVal" , fVal)
            #print(type(fVal))
            
            #print("fVal" , fVal)
            #print("tSum" , tSum)
            #print("i" , i)

except:
    print('')


#calc the average

average = tSum / i
print("Average spam confidence:" , average);

print("Done")