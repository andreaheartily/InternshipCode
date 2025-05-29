''' print ("Hello, how are you doing?")

# Variables and datatypes
diary_entry_date="25/05/2025" #string
mood_level=8 #integer
# to set a constant value just make the first letter of the variable name a capital letter e.g MOOD_LEVEL=8
sleep_hours=7.5 #float
is_favorite=True #boolean
# Fastrings- an elegant and simpler way of writing a statement
print(f"Date:{diary_entry_date}")
print(f"Mood:{mood_level}/10")
print(f"Sleep:{sleep_hours}hours")
print(f"favorite:{is_favorite}") #Python figures out the type automatically!
entry_text="Had an amazing day learning Python!"
print(type(entry_text)) #<class'str'>

#User input
print("Welcome to your smart Diary!")
name=input("What's your name?")
date=input("What's today's date?")
mood=input("Rate your mood(1-10):")
entry=input("Tell me about your day;")
print("\n" + "="*40) 
print(f"Date:{date}")
print(f"Author:{name}")
print(f"Mood:{mood}/10")
print(f"Entry:{entry}")
print("="*40)
print("Entry saved!") 

#Converting user input for diary
mood_str= input("Rate your mood (1-10):")
mood_num= int(mood_str)# Convert to integer
print(f"Your mood level: {mood_num}")
#Calculate average mood over time
total_mood= mood_num + 7 + 9
#Previous entries
average= total_mood/3
print(f"Average mood: {average:1f}")
#Validation example
 try: rating= int(input("Mood(1-10):"))
if 1 <= rating <= 10: print("Valid rating!")
else: print("Please enter 1-10")
except ValueError: print("Please enter a number!") 

#Date parshing for diary
date_input= "25/05/2025"
day = date_input[0:2] #25
month = date_input[3:5] #05
year = date_input[6:10] #2025
print(f"Day:{day}, Month:{month}, Year:{year}")
# Processing diary text
entry = "Today was AMAZING! I learned Python!"
clean_entry= entry.strip().lower()
words= clean_entry.strip()
word_count= len(words)
print(f"Word count:{word_count}")
print(f"Word:{words}") 


# Dictionaries
person= {
    "name" : "Alice",
    "age" : 25,
    "city" : "New York"
} # the item on the left is the key and on the right is the value
# .item is used to print out the key-value pair, .key prints the key, .value prints the value

#Boolean data type and logical operators
x=5
y=10
print(x>0 and y>0)
print(x>10 or y<20)
print(not (x==5))

#Conditional statements
age=20
if age >= 18:
    print("You are an adult")

if age >= 18:
    print("Adult")
else:
    print("Minor")

marks = 85
if marks>= 90:
    print("A")
elif marks>= 80:
    print("B")
elif marks>= 70:
    print("C")
else:
    print("Null")

#Loops
#while loop
i=0
while i<5:
    print(i)
    i+=1 # i=i+1, i++ 

#for loop
for i in range (5):
    print (i) # prints values from 0-5

#Nested loops
for i in range(2):
    for j in range(3):
        print(f"i={i}, j={j}")

#Functions
def greet ():
    print("Hello")
greet()

#parameters and arguments
def greet(name):
    print(f"Hello, {name}!")
greet("Alice")

#Return 
def square(x):
    return x*x
result = square(5)
print (result)

#Data Structures

#Adding to a list
ds = {
    'Mark',
    'John',
    'Matthew'
}
#using append
ds.append = ('Alice')
#using extend
newds = ('Peter','Phillip')
ds.extend(newds)
#using insert

print(ds)

#Finding and counting 
weekly_attendes = ['Alice', 'Bob', 'Alice', 'Charlie', 'Alice']
#count occurences
alice_count = weekly_attendes.count('Alice')
print(f"Alice count: {alice_count}")

#Removing elements
weekly_attendes.remove('Bob') #remove first occurence 

#Sorting and reversing

#LIFO(stack)

#FIFO(queue)

apps = ['instagram', 'tiktok', 'duolingo', 'candy_crush', 'banking_app']
del apps[3]
print(apps)

#Sets
set_one = [1,2,4,9,16]
set_two = [1,2,3,5,7,9]
print(f"Union: {set_one | set_two}")
print(f"Intersection: {set_one & set_two}")
print(f"Difference: {set_one - set_two}")
print(f"Symmetric difference: {set_one ^ set_two}")

with open (r"C:\Users\andre_eergmfm\OneDrive\Documents\Programming text files\file.txt", 'a') as file:
    file.write('This is from a report about the internet of things.')

with open (r"C:\Users\andre_eergmfm\OneDrive\Documents\Programming text files\file.txt", 'r') as file:
    content = file.read()
    print(content)

with open (r"C:\Users\andre_eergmfm\OneDrive\Documents\Programming text files\sample.txt", 'w') as file:
    file.write('This is from a report about the internet of things.')

with open (r"C:\Users\andre_eergmfm\OneDrive\Documents\Programming text files\sample.txt", 'r') as file:
    content = file.read()
    print(content)

student_info = {
    'name' : 'Sarah',
    'age' : 16,
    'subjects' : ['Math', 'Science', 'Computer Science'],
    'gpa' : 3.8
}

def display_student(student):
    print(f"Student : {student['name']}")
    print(f"Age: {student['age']}")
    print("Subjects:")
    for subject in student['subjects']:
        print(f" - {subject}")
    
    if student['gpa'] >= 3.5:
        print("Great job! You are doing excellent!")
    else:
        print("Keep working hard!")

display_student(student_info) 

# Object Oriented Programming

def _init_(self,name,age): # init is a constructor, initialises the object with starting values, ensures every objest starts with the necessary attributes
    self.name = name
    self.age = age
    Animal = Animal("Dog", 14)
print(f"This is a {name} and it's {age} years old.")'''

class Student:
    # ... attributes from above ...
    
    # Method that doesn't change anything (getter)
    def get_info(self):
        return f"{self.name} - Grade {self.grade}"
    
    # Method that changes object state (setter)
    def set_gpa(self, new_gpa):
        if 0.0 <= new_gpa <= 4.0:
            self.gpa = new_gpa
        else:
            print("Invalid GPA! Must be between 0.0 and 4.0")
    
    # Method that performs an action
    def celebrate_birthday(self):
        self.age += 1
        print(f"🎉 Happy Birthday {self.name}! Now {self.age} years old!")

# Using methods
student = Student("Emma", 16, 10)
print(student.get_info())     # Emma - Grade 10
student.set_gpa(3.8)         # Sets GPA to 3.8
student.celebrate_birthday() # 🎉 Happy Birthday Emma! Now 17 years old!

'''class Student:
    def _init_(self, name, age, grade):
        # These are attributes
        self.name = name      # String attribute
        self.age = age        # Integer attribute
        self.grade = grade    # Integer attribute
        self.subjects = []    # List attribute
        self.gpa = 0.0       # Float attribute'''