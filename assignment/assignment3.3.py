i = input("Please enter a Score between 0.0 and 1.0: ")

try:
    score = float(i)
except:
    print("Error, please enter numeric input")
    print("quit")
    quit()

if score <= 1 and score >= 0:
    #Score in Range
    #print(score)
    if score >= 0.9:
        print("A")
    elif score >= 0.8:
        print("B")
    elif score >= 0.7:
        print("C")
    elif score >= 0.6:
        print("D")
    elif score < 0.6:
        print("F")

else:
    #Score out of Range
    print("Error, please enter a number between 0.0 and 1.0. Your input is out of range")