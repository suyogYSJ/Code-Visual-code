marks = {} 
total = 0 

subjects = ["Sub 1", "sub 2", "sub 3", "sub 4", "sub 5"] 
 
for subject in subjects: 
    marks[subject] = input("Enter " + subject + " marks : ") 
 
for key in marks.values(): 
    total += int(key) 
 
percentage = (total*100) / 500  
 
# if percentage >= 90: 
#     print("A") 
# elif percentage >= 80: 
#     print("B") 
# elif percentage >= 50: 
#     print("C") 
# else: 
#     print("Fail") 
if(percentage>=90):
    print("Grade: A")
elif(percentage>=80&percentage<90):
    print("Grade: B")
elif(percentage>=70&percentage<80):
    print("Grade: C")
elif(percentage>=60&percentage<70):
    print("Grade: D")
else:
    # print("Grade: F")
    print(f"With a percentage of {percentage}%")

