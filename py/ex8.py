# 1. Create a starting grocery list
fruits = ["apple", "banana", "orange"]
print("Starting list:", fruits)

# 2. Append: Add an item to the end
fruits.append("grape")
print("After append:", fruits)

# 3. Remove: Remove an item by its name
fruits.remove("banana")
print("After remove:", fruits)

# 4. Len: Count how many items are in the list
total_items = len(fruits)
print("Total number of items:", total_items)

# 5. Concatenation (+): Glue a new list to our old list
extra_items = ["mango", "kiwi"]
final_list = fruits + extra_items
print("After gluing lists together:", final_list)

