




# Convert 1-10 to a string representation
def numbers1to10(num):
    dict1to10 = {0:'Zero', 1:'One', 2:'Two', 3:'Three', 4:'Four', 5:'Five', 6:'Six', 7:'Seven', 8:'Eight', 9:'Nine', 10:'Ten'}
    return dict1to10[num]

# Convert 11-19 to a string representation
def numbers11to19(num):
    dict11to19 = {11:'Eleven', 12:'Twelve', 13:'Thirteen', 14:'Fourteen', 15:'Fifteen', 16:'Sixteen', 17:'Seventeen', 18:'eighteen', 19:'Nineteen'}
    return dict11to19[num]

# Convert 20-99 to a string representation
def numbers20to99(num):
    dict20to99 = {20:'Twenty', 30:'Thirty', 40:'Forty', 50:'Fifty', 60:'Sixty', 70:'Seventy', 80:'Eighty', 90:'Ninety', 100:'Hundred'}
    tens = (num//10) * 10
    ones = num%10
    output = dict20to99[tens]
    if ones > 0:
        output += " "
        output += numbers1to10(ones)
    return output

# Convert 100-999 to a string representation
def numbers100to999(num):

    hundreds = num//100
    tens = num%100
    print(f"Huns:{hundreds} Tens: {tens}")
    output = numbers1to10(hundreds)
    output += " Hundreds"
    if tens > 0:
        output += " "
        output += numbers20to99(tens)

    return output

# Converts numbers  from 0-999 to a string representation
def convert_number_phrase(num):
    output = ''
    if -1 < num < 11:
        print(num)
        output = numbers1to10(num)
    elif 11 <= num <20:
        print(num)
        output = numbers11to19(num)
    elif 20 <= num <= 99:
        print(num)
        output = numbers20to99(num)
    elif 100 <= num < 1000:
        print(num)
        print(numbers100to999(num))

    return output


print(convert_number_phrase(4))
print(convert_number_phrase(19))
print(convert_number_phrase(33))
print(convert_number_phrase(99))

print(convert_number_phrase(100))
print(convert_number_phrase(333))
print(convert_number_phrase(999))




# Convert 1-9 to a string representation
def roman_numbers1to9(num):
    print(num)
    dict1to9 = {1:'I', 2:'II', 3:'III', 4:'IV', 5:'V', 6:'VI', 7:'VII', 8:'VIII', 9:'IX'}
    return dict1to9[num]

# Convert 10-90 to a string representation
def roman_numbers10to90(num):
    print(num)
    dict10to90 = { 10:'X', 20:'XX', 30:'XXX', 40:'XL', 50:'L', 60:'LX', 70:'LXX', 80:'LXXX', 90:'XC'}
    tens = (num//10) * 10
    ones = num%10
    output = dict10to90[tens]
    if ones > 0:
        output += roman_numbers1to9(ones)
    return output

# Convert 10-90 to a string representation
def roman_numbers100to900(num):
    print(num)
    dict100to900 = { 100:'C', 200:'CC', 300:'CCC', 400:'CD', 500:'D', 600:'DC', 700:'DCC', 800:'DCCC', 900:'CM'}
    hundreds = (num//100) * 100
    num = num%100
    tens = (num//10) * 10
    ones = num%10
    output = ''

    if hundreds > 0:
        output += dict100to900[hundreds]

    if tens > 0:
        output += roman_numbers10to90(tens)

    if ones > 0:
        output += roman_numbers1to9(ones)
    return output

def roman_numbers1000to5000(num):
    print(num)
    if num > 5000:
        return "Too large"

    dict1000to5000 = { 1000:'M', 2000:'MM', 3000:'MMM', 4000:'MMMM', 5000:'MMMMM'}
    thousands = (num//1000) * 1000
    num = num%1000
    hundreds = (num//100) * 100
    num = num%100
    tens = (num//10) * 10
    ones = num%10
    output = ''

    if thousands > 0:
        output = dict1000to5000[thousands]

    if hundreds > 0:
        output += roman_numbers100to900(hundreds)

    if tens > 0:
        output += roman_numbers10to90(tens)

    if ones > 0:
        output += roman_numbers1to9(ones)
    return output

print(roman_numbers1to9(4))
print(roman_numbers10to90(19))
print(roman_numbers10to90(33))
print(roman_numbers10to90(99))
print(roman_numbers100to900(100))
print(roman_numbers100to900(999))
print(roman_numbers1000to5000(1001))
print(roman_numbers1000to5000(3000))
print(roman_numbers1000to5000(4999))
print(roman_numbers1000to5000(5000))