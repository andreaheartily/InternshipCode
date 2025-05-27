'''print ("Hello, how are you doing?")

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
except ValueError: print("Please enter a number!")'''

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


