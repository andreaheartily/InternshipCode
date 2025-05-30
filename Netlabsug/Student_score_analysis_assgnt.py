# A program that analyzes student scores

#Function for student input
def get_student_data():
    student = {
        'name' : input("What's your name? "),
        'score' : [
            float(input("What's your score for test1?")),
        ]
    }
    return student
#Exception handling for score input
try:
 score = float("ninety")
except ValueError:
    print("Please enter a number, not text!")
try:
    if 0>= score <=100:
        print("score")
except ValueError:
    print("Please enter a number from 0 to 100")

#Display of student data
student_data=get_student_data()
print("\nStudent Data:")
print(student_data)

#Function for grade score ranges
def calculate_grade(score):
    if score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    elif score >= 80:
        print("C")
    else:
        print("F")

#Function for student statistics
def class_statistics(*score):
    minimum = min(score),
    maximum = max(score),
    average = sum(score)/len(score)
    return minimum, maximum, average

#Display of student score and grade
for name, score in student_data.items():
    grade = calculate_grade(score)
    print(f"{name} has a score of {score} and a grade of {grade}")

#Function for filtering out top performers
def filter(student):
    score=list(student.value())
    average= sum(score)/len(score)
    dict(filter (lambda item:item[1]>average),student.item[1])

#Function for sumation of scores
def sum_scores(n):
    if n == 1:
        return 1
    else:
        return n + sum_scores(n-1)

#Function for user interaction
def user_interaction(student):
    name = str(input("Enter a name: "))
    #add code for score input then append to student dict
    if name in student[name]:
        score = student[score]
        grade = calculate_grade(score)
        print(f"{name} has a score of {score} and a grade of {grade}")
    else:
        print(f"{name} does not exist.")

#Exception handling for input
try:
    student={}
    name= student.item(0)
    if name in student[name]:
        print([name])
except:
    print("This name exists in the system")










