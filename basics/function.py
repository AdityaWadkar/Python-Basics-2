def computepay(h,r):
    pay = 0
    overtime = 0
  
    if h > 40:
        overtime = h - 40

        pay = ((h - overtime ) * r) + (overtime * r * 1.5)
    else:
        pay =  (h * r)
    


    #print("Pay: ", pay)
    return pay


payv = computepay(45, 10.5)
print("Pay: " , payv)