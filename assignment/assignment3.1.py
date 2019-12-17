pay = 0
overtime = 0
h = 0
r= 0

#### hors
hrs =  input("Enter Hours:")
try:
    h = float(hrs)
except:
    print("Error, please enter numeric input")
    print("quit")
    quit()

#### rate
rate =  input("Enter Rate:")
try:
    r = float(rate)
except:
    print("Error, please enter numeric input")
    print("quit")
    quit()




if h > 40:
    overtime = h - 40

    pay = ((h - overtime ) * r) + (overtime * r * 1.5)
else:
    pay =  (h * r)
   


print("Pay: ", pay)
