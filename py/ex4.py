score = 0

Quiz1 = input("What comes after rain: ")

if Quiz1 == "rainbow":
    print("correct! you got")
    score = score + 1
    print("your score is", {score})
    
else: 
    print("Wrong")

Quiz2 = input("What is the largest organ in the human body: ")

if Quiz2 == "skin":
    print("correct! you got")
    score = score + 10
    print("your score is", {score})
    
else: 
    print("Wrong")

Quiz3 = input("what is the name of the auxiliary language created in 1887 by L. L. Zamenhof, intended to be a universal second language?: ")

if Quiz3 == "esperanto":
    print("correct! you got")
    score = score + 100
    print("your score is", {score})
    
else: 
    print("Wrong")
