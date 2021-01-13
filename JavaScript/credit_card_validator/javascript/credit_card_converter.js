/*
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
*/

// Select the generate passord button and add a Event listener for click actions on the button
let validator_button = document.querySelector("#validate_credit_card");
console.log("Got Button: " + validator_button)
validator_button.addEventListener("click", function() {
    validate_credit_card()
});


function validate_credit_card() {
    // Convert the input string into a list of ints
    var credit_card_number_div = document.querySelector("#credit_card_number");
    console.log("Value Feild: " + credit_card_number_div.value)
    console.log("Card Field Value Length: " + credit_card_number_div.value.length)
    if (credit_card_number_div.value.length > 0) {
        credit_card_number = credit_card_number_div.value
        console.log("Value Credit Card No.: " + credit_card_number)
    } else {
        credit_card_number = credit_card_number_div.placeholder
        console.log("Placeholder Credit Card No.: " + credit_card_number)
    }
    console.log("Incoming Credit Card No.: " + credit_card_number)
    cred_list = credit_card_number.split(" ")
    num_cred_list = []
    
    for (var i = 0; i < cred_list.length; i++) {
        num_cred_list.push(parseInt(cred_list[i]))
    }
    console.log("Card Array of ints: " + num_cred_list)
        
    // Slice off the last digit. That is the check digit.
    last_dig = num_cred_list.pop()
    console.log("Last Digit: " + last_dig)
    // Reverse the digits.
    num_cred_list.reverse()
    console.log("Reserver card: " + num_cred_list)

    // Double every other element in the reversed list.
    for (var i = 0; i < num_cred_list.length; i++) {
        if ((i % 2) == 0) {
            num_cred_list[i] = num_cred_list[i] + num_cred_list[i]
        }
    }
    console.log("Double elements: " + num_cred_list)

    // Subtract nine from numbers over nine.
    for (var i = 0; i < num_cred_list.length; i++) {
        if (num_cred_list[i] > 9) {
            num_cred_list[i] -= 9
        }
    }
    console.log("Subtract numbers from 9 or greater: " + num_cred_list)

    // Sum all values.
    var sum = 0
    for (num = 0; num < num_cred_list.length; num++) {
        sum += num
        console.log(sum)
    }


    // Take the second digit of that sum.
    var remainder = sum % 10
    console.log("remainder: " + remainder)

    var validates = false
    let credit_validation = document.querySelector("#card_validated");
    if (remainder == last_dig) {
        console.log("Credit card validates")
        validates = true
        credit_validation.innerText = "Credit card validates"
    } else {
        console.log("Card doens't validate")
        credit_validation.innerText = "Card doens't validate"
    }
    return validates
}

    // If that matches the check digit, the whole card number is valid.
    // For example, the worked out steps would be:
