# A program that analyzes student scores

#Function for student input
def get_student_data():
    student = {
        'name' : input("What's your name? "),
        'scores' : [
            float(input("What's your score for test1?")),
            #float(input("What's your score for test2?"))
        ]
    }
    return student

student_data=get_student_data()
print("\nStudent Data:")
print(student_data)

def calculate_grade(score):
    if score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    elif score >= 80:
        print("C")
    else:
        print("F")

def class_statistics(*scores):
    minimum = min(scores),
    maximum = max(scores),
    average = sum(scores)/len(scores)
    return minimum, maximum, average

for name, score in student_data.items():
    grade = calculate_grade(score)
    print(f"{name} has a score of {score} and a grade of {grade}")

def filter(student):
    score=list(student.value())
    average= sum(score)/len(score)
    dict(filter (lambda item:item[1]>average),student.item[1])

def sum_scores(n):
    if n == 1:
        return 1
    else:
        return n + sum_scores(n-1)

def user_interaction(student):
    name = str(input("Enter a name: "))
    
    if name in student[name]:
        score = student[score]
        grade = calculate_grade(score)
        print(f"{name} has a score of {score} and a grade of {grade}")
    else:
        print(f"{name} does not exist.")








