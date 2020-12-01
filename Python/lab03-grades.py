

def ifbetweengrade(grade):
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


def modgrade(grade):
    remainder = grade % 10
    higlow = ""
    if grade < 100:
        if remainder < 3:
            highlow = "-"
        elif remainder > 7:
            highlow = "+"
        else:
            highlow = "" 
    else:
       highlow = "++"  

    return highlow

def inputgrade():
    grade = input("Enter grade value between 0-100: ")
    if grade.isdigit():
        return int(grade)
    else:
        grade = inputgrade()
    return grade


def main():
    running = True
    while running == True:
        value = input("Enter Y or N if you want to get a letter grade: ")

        if value == "N" or value == "n":
            break

        grade = inputgrade()
        letter_grade = ifbetweengrade(grade)
        grade_mod = modgrade(grade)

        print(f"You recieved {letter_grade}{grade_mod}")

main()