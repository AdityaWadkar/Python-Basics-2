# words.txt


fname = input('Enter the file name: ')


try:
    fhand = open('../files/' + fname)
except:
    print('File could not be opend:' , fname)

try:
    for line in fhand:
        line = line.rstrip().upper()
        print(line)
except:
    print('')
