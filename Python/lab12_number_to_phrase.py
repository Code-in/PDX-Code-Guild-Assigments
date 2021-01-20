




# Convert 1-10 to a string representation
def ones(num):
    dict1to10 = {0:'Zero', 1:'One', 2:'Two', 3:'Three', 4:'Four', 5:'Five', 6:'Six', 7:'Seven', 8:'Eight', 9:'Nine', 10:'Ten'}
    return dict1to10[num]

# Convert 11-19 to a string representation
def teens(num):
    dict11to19 = {11:'Eleven', 12:'Twelve', 13:'Thirteen', 14:'Fourteen', 15:'Fifteen', 16:'Sixteen', 17:'Seventeen', 18:'eighteen', 19:'Nineteen'}
    return dict11to19[num]

# Convert 20-99 to a string representation
def tens(num):
    dict20to99 = {1: 'Ten', 2:'Twenty', 3:'Thirty', 4:'Forty', 5:'Fifty', 6:'Sixty', 7:'Seventy', 8:'Eighty', 9:'Ninety', 10:'Hundred'}
    return dict20to99[num]

# need to convert to use this which will require me to do a string len and offset to get the // (Floor) devidor
dict10to100000 = {3:100, 4:1000, 5:10000, 6:100000 }
dict10to100000Label = {3: 'Hundreds', 4: 'Thousands', 5: 'Thousands', 6: 'Hundred Thousand' }

# Needs work for compund ranges like hundres, thousands, etc...
def hundreds_to_hundred_thousand(num):
    output = ''
    str_num = str(num)
    str_len = len(str_num)
    if(str_len >= 3): # process numbers greater than 99
        floor = (num//dict10to100000[str_len])
        output = dict10to100000Label[str_len]
    elif (str_len < 3):
        if 20 <= num <= 99:
            output += tens(num%10)
            num = num%10
        if num < 1:
            #return format_out(orig_num, output)
            output += ' '

        if 10 < num < 20:
            output += teens(num)

        else: 
            output += ones(num)

    return output



# Convert 100-999 to a string representation
def hundreds(num):
    output = ''
    hundreds = (num//100)
    output = ones(hundreds)
    output += " Hundred"
    return output

def thousands(num):
    output = ''
    hundreds = (num//1000)
    output = ones(hundreds)
    output += " Thousand"
    return output

def tensofthousands(num):
    output = ''
    ten = (num//10000)
    output = tens(ten)
    output += " Thousand"
    return output

def hundredsofthousands(num):
    output = ''
    hundreds = (num//100000)
    output = ones(hundreds)
    output += " Hundred Thousand"
    return output


def format_out(num, string):
    return f"Number: {num} ---> Written Number: {string}"

# Converts numbers  from 0-999 to a string representation
def convert_number_phrase(num):
    orig_num = num
    output = ''

    if 100000 <= num < 1000000:
        output += hundredsofthousands(num)
        num = num%100000
        if num < 1:
            return format_out(orig_num, output)
        output += ' '

    if 10000 <= num < 100000:
        output += tensofthousands(num)
        num = num%10000
        if num < 1:
            return format_out(orig_num, output)
        output += ' '

    if 1000 <= num < 10000:
        output += thousands(num)
        num = num%1000
        if num < 1:
            return format_out(orig_num, output)
        output += ' '

    if 100 <= num < 1000:
        output += hundreds(num)
        num = num%100
        if num < 1:
            return format_out(orig_num, output)
        output += ' '

    if 20 <= num <= 99:
        output += tens(num%10)
        num = num%10
        if num < 1:
            return format_out(orig_num, output)
        output += ' '

    if 10 < num < 20:
        output += teens(num)

    else: 
        output += ones(num)

    return format_out(orig_num, output) 



# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Numbers converted to Roman numbers system
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Convert 1-9 to a string representation
def roman_numbers1to9(num):
    dict1to9 = {1:'I', 2:'II', 3:'III', 4:'IV', 5:'V', 6:'VI', 7:'VII', 8:'VIII', 9:'IX'}
    return dict1to9[num]

# Convert 10-90 to a string representation
def roman_numbers10to90(num):
    dict10to90 = { 1:'X', 2:'XX', 3:'XXX', 4:'XL', 5:'L', 6:'LX', 7:'LXX', 8:'LXXX', 9:'XC'}
    return dict10to90[num]

# Convert 10-90 to a string representation
def roman_numbers100to900(num):
    dict100to900 = { 1:'C', 2:'CC', 3:'CCC', 4:'CD', 5:'D', 6:'DC', 7:'DCC', 8:'DCCC', 9:'CM'}
    return dict100to900[num]

def roman_numbers1000to5000(num):
    dict1000to5000 = { 1:'M', 2:'MM', 3:'MMM', 4:'MMMM', 5:'MMMMM'}
    return dict1000to5000[num]



def convert_numbers_to_roman_numbers(num):
    orig_num = num
    output = ''
    
    if num > 5000:
        print("Numbers greater than 5000 cannot be computed!")
        num = num%1000

    if 999 < num <= 5000:
        thousands = (num//1000)
        num = num%1000
        output = roman_numbers1000to5000(thousands)

    if 99 < num <= 999:
        hundreds = (num//100)
        num = num%100
        output += roman_numbers100to900(hundreds)

    if 9 < num <= 99:
        tens = (num//10)
        num = num%10
        output += roman_numbers10to90(tens)

    if 1 < num <= 9:
        output += roman_numbers1to9(num)

    return f"Number:{orig_num} Roman:{output}"


print(hundreds_to_hundred_thousand(4))
print(hundreds_to_hundred_thousand(19))
print(hundreds_to_hundred_thousand(33))
print(hundreds_to_hundred_thousand(99))
print(hundreds_to_hundred_thousand(100))
print(hundreds_to_hundred_thousand(333))
print(hundreds_to_hundred_thousand(999))
print(hundreds_to_hundred_thousand(101))
print(convert_number_phrase(111))
print(convert_number_phrase(500))
print(convert_number_phrase(1000))
print(convert_number_phrase(1001))
print(convert_number_phrase(9999))
print(convert_number_phrase(10000))
print(convert_number_phrase(10001))
print(convert_number_phrase(99999))
print(convert_number_phrase(100000))
print(convert_number_phrase(100001))
print(convert_number_phrase(999999))
print("Roman Numbers Below ===================================")
print(convert_numbers_to_roman_numbers(4))
print(convert_numbers_to_roman_numbers(19))
print(convert_numbers_to_roman_numbers(33))
print(convert_numbers_to_roman_numbers(99))
print(convert_numbers_to_roman_numbers(100))
print(convert_numbers_to_roman_numbers(999))
print(convert_numbers_to_roman_numbers(1001))
print(convert_numbers_to_roman_numbers(3000))
print(convert_numbers_to_roman_numbers(4999))
print(convert_numbers_to_roman_numbers(5000))
print(convert_numbers_to_roman_numbers(5001))