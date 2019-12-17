data = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
atPos = data.find('@') +1 
spacePos = data.find(' ' , atPos) 
print (data[atPos:spacePos])