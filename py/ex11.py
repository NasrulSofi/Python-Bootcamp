student_records = {
    "student_001": {
        "name": "John",
        "age": 19,
        "major": "Computer Science",
        "grades": [85, 92, 78]
    },

    "student_002": {
        "name": "Sarah",
        "age": 20,
        "major": "Biology",
        "grades": [90, 88, 95]
    }
}       

# new data for student_003
new_student_data = {
    "name": "Mike",
    "age": 18,
    "major": "Mathematics",
    "grades": [82, 79, 91]
}
# Adding new student record for student_003
student_records["student_003"] = new_student_data
student_records["student_001"]["age"] = 20

for student_id in student_records:
    name = student_records[student_id]["name"]
    major = student_records[student_id]["major"]
    print(f"Student ID:{student_id}, Name: {name}, Major: {major}")



