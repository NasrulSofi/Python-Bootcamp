grades = [                      #<-- tuple inside a list
    ("Alice", "Math", 85),
    ("Bob", "Science", 92),
    ("Alice", "Science", 78),
    ("Charlie", "Math", 90),
    ("Bob", "Math", 88),
    ("Alice", "English", 95)]

unique_students = set()
unique_subjects = set()

for item in grades:
    student_name = item[0]
    subject_name = item[1]
    
    unique_students.add(student_name)   
    unique_subjects.add(subject_name)   

print("Unique Students:", unique_students)
print("Unique Subjects:", unique_subjects)