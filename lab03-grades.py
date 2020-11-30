
grade = int(input("Enter grade value between 0-100: "))
letter_grade = "F"

if grade < 59:
    letter_grade = "F"
elif 60 <= grade < 70:
    letter_grade = "D"   
elif 70 <= grade < 80:
     letter_grade = "C"      
elif 80 <= grade < 90:
    letter_grade = "B"   
else:
    letter_grade = "A" 

print(f"You recieved {letter_grade}")