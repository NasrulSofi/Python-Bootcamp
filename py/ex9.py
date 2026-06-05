numlist = [22, 3, 12, 14, 19, 6, 1, 8, 10]

biggest = numlist[0]
smallest = numlist[0]

for num in numlist:
    if num > biggest:
        biggest = num
    if num < smallest:  
        smallest = num

print("Biggest number:", biggest)
print("Smallest number:", smallest)