# A program that analyzes student scores

#Function for student input
def get_student_data():
    student = {
        'name' : input("What's your name? "),
        'scores' : [
            float(input("What's your score for test1?")),
            float(input("What's your score for test1?")),
            float(input("What's your score for test1?"))
        ]
    }
    return student

student_data=get_student_data

print("\nStudent Data:")
print(f"Name: {student_data['name']}")
print(f"Scores: {student_data['scores']}")


