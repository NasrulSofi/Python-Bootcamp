def Find_TempF(TempC):
    return (TempC * 9/5) + 32

TempC = float(input("Enter the temperature in Celsius: "))
TempF = Find_TempF(TempC)
print("The temperature in Fahrenheit is:", TempF)