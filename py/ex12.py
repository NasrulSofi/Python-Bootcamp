

def find_prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        return True

    else:
        return False

num = int(input("Enter a number: "))
if find_prime(num):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")
