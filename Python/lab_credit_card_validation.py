
'''
Lab: Credit Card Validation

Let's write a function which returns whether a string containing a credit card number is valid as a boolean. The steps are as follows:

Convert the input string into a list of ints
Slice off the last digit. That is the check digit.
Reverse the digits.
Double every other element in the reversed list.
Subtract nine from numbers over nine.
Sum all values.
Take the second digit of that sum.
If that matches the check digit, the whole card number is valid.
For example, the worked out steps would be:

4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5
4 5 5 6 7 3 7 5 8 6 8 9 9 8 5
5 8 9 9 8 6 8 5 7 3 7 6 5 5 4
10 8 18 9 16 6 16 5 14 3 14 6 10 5 8
1 8 9 9 7 6 7 5 5 3 5 6 1 5 8
85
5
Valid!
'''

def validate_credit_card(card):
    # Convert the input string into a list of ints
    cred_list = card.split(" ")
    num_cred_list = []
    for letter in cred_list:
        num_cred_list.append(int(letter))
    # Slice off the last digit. That is the check digit.
    last_dig = num_cred_list.pop()
    print(f"Last Digit: {last_dig}")
    # Reverse the digits.
    num_cred_list.reverse()
    print(f"Reserver card {num_cred_list}")

    # Double every other element in the reversed list.
    for i in range(len(num_cred_list)):
        if i % 2 == 0:
            num_cred_list[i] = num_cred_list[i] + num_cred_list[i]
    print(f"Double elements: {num_cred_list}")

    # Subtract nine from numbers over nine.
    for i in range(len(num_cred_list)):
        if num_cred_list[i] > 9:
            num_cred_list[i] -= 9
    print(num_cred_list)

    # Sum all values.
    sum = 0
    for num in num_cred_list:
        sum += num
    print(sum)

    # Take the second digit of that sum.
    remainder = sum % 10
    print(f"remainder: {remainder}")

    validates = False
    if remainder == last_dig:
        print("Credit card validates")
        validates = True
    else:
        print("Card doens't validate")

    return validates

    # If that matches the check digit, the whole card number is valid.
    # For example, the worked out steps would be:


print(validate_credit_card('4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5'))

