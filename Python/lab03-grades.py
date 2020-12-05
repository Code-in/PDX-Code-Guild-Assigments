
# Convert grade from interger to letter grade
def if_between_grade(grade):
    letter_grade = "F"

    if grade <= 59:
        letter_grade = "F"
    elif 60 <= grade < 70:
        letter_grade = "D"   
    elif 70 <= grade < 80:
        letter_grade = "C"      
    elif 80 <= grade < 90:
        letter_grade = "B"   
    else:
        letter_grade = "A" 

    return letter_grade

# Convert letter grade to a +/- letter grade based on there score
def mod_grade(grade):
    remainder = grade % 10
    higlow = ""

    if grade <= 59:
        highlow = "" 
    elif grade < 100:
        if remainder < 3:
            highlow = "-"
        elif remainder > 7:
            highlow = "+"
        else:
            highlow = ""
    else:
       highlow = "++" 


    return highlow

# Ask the user for a integer grade to work with
def input_grade():
    while True:
        grade = input("Enter grade value between 0-100: ")
        if grade.isdigit():
            return int(grade)


# Main function where all the methods will be called if the user want to get a letter
def main():

    running = True
    while running == True:
        value = input("Enter Y or N if you want to get a letter grade: ")
        if value in ['n', 'N', 'No', 'NO', 'no']:
            break
        elif value.isascii and value in ['y', 'Y', 'Yes', 'YES', 'yes']:
            grade = input_grade()
            letter_grade = if_between_grade(grade)
            grade_mod = mod_grade(grade)
            print(f"You recieved {letter_grade}{grade_mod}")



main()