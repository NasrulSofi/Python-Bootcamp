import os
import sys
import datetime
import random


#sys.path.append(os.path.dirname(os.path.dirname(os.path)))

now = datetime.datetime.now()
today = datetime.date.today()
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")

print(f"Now Date: {now}")
print(f"Today's Date: {today}")
print(f"Formatted Date: {formatted_date}")

random_number = random.randint(1, 100)
random_choice = random.choice(['apple', 'banana', 'orange'])
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)

print(f"Random Number: {random_number}")
print(f"Random Choice: {random_choice}")
print(f"Shuffled Numbers: {numbers}")