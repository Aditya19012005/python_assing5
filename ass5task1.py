
def get_student_marks():
    marks = {
        "Alice": 85,
        "Adi": 92,
        "Charlie": 78,
        "Zen": 90,
        "Eve": 88
    }

    name = input("Enter the student's name: ")

    if name in marks:
        print(f"{name}'s marks: {marks[name]}")
    else:
        print("Student not found in the records.")

get_student_marks()
