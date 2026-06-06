for i in range(2, 20):# i in range 
    prime = True # treat i as prime first
    
    for j in range(2, i): # j in range
        if i % j == 0:  # using Modulo, to divide i by j,finding 0 leftover
            prime = False # if no leftover, then i is not prime
            break # no idea why we need to break, AI did it for me

    if prime: # if i is prime, print it
        print(i) 