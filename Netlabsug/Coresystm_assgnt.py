# Core System

#Personalized greeting
name=input("What's your name?")
print(f"Hello, {name}")

#Diary entries, using input function to get interactive user output
gender=input("What's your gender?")
dailygoal=input("What's your goal for today?")
weather=input("What's today's weather?")
hobby=input("What's your hobby?")
creativeoutlet=input("What's your creative outlet?")

#Display of entries, formatting and displaying user input
print("\n" + "="*40) 
print(f"Name:{name}")
print(f"Gender:{gender}")
print(f"weather:{weather}")
print(f"Daily goal:{dailygoal}")
print(f"Hobby:{hobby}")
print(f"Creative outlet:{creativeoutlet}")
print("="*40  + "\n" )

#Average mood, asking for mood, calculating the average mood
mood_str= input("Rate your mood (1-10):") #getting user input for mood
mood_num= int(mood_str)# Converting to integer
print(f"Your mood level: {mood_num}")
#Calculate average mood over time
total_mood= mood_num + 4 + 6 # 4 and 6 are previous entries
average= total_mood/3
print(f"Average mood: {average:1f}\n")

#Longest entry
entries = {
    "Name": name,
    "Gender": gender,
    "Weather": weather,
    "Daily goal": dailygoal,
    "Hobby": hobby,
    "Creative outlet": creativeoutlet
 } # Dictionary for storage of the different entries

#Function to find the longest entry and it's length
longest_label, longest_value = max(entries.items(), key=lambda item: len(str(item[1]))) # max is used to find the maximum value, .items returns a view object containing all key-value pairs, key customizes the comparision, lambda takes the value part of the key value item which is 1 and the length of the value is calculated in it's string format.
#Display
print(f"The longest entry is '{longest_label}': {longest_value} (Length: {len(longest_value)})\n")
# longest_label, longest_value is a tuple unpacked into two different variables.

#Word count for each entry
#Calculation
word_counts = {label: len(value.split()) for label, value in entries.items()} # new dictionary(word_counts) created, 
#Display using for loop
print("Word Count for Each Entry:")
for label, count in word_counts.items():
    print(f"{label}: {count} words")
