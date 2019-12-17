# mbox.txt
# mbox-short.txt


fname = input('Enter the file name: ')

open()

try:
    fhand = open('../files/' + fname)
except:
    print('File could not be opend:' , fname)

try:
    for line in fhand:
        line = line.rstrip()
        if line.startswith('From') :
            print(line)
except:
    print('')
