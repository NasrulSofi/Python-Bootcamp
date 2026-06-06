heightcm = int(input("Height in CM: "))
weightkg = int(input("Weight in KG: "))
bmi = weightkg / (heightcm/100)**2

if bmi <= 18.5:
    print("Underweight.")
elif bmi >=18.5 and bmi <24.9:
    print("Normal.")
elif bmi >=24.9 and bmi <29.9:
    print("Overweight.")
elif bmi >=29.9 and bmi <30:
    print("Obesity.")
else: 
    print("Morbid Obesity")
