// 

let convert_button = document.querySelector(".action_button")
console.log(convert_button)
convert_button.addEventListener("click", function(event) {
    let number_to_convert = document.querySelector(".number_to_convert")
    console.log(number_to_convert.value)
    phrase = convert_number_phrase(number_to_convert.value)
    document.querySelector(".phrase_container").innerHTML = "<p> Number to Phrase: " + phrase + "</p>"

})

// Convert 1-10 to a string representation
function ones(num){
    dict1to10 = {0:'Zero', 1:'One', 2:'Two', 3:'Three', 4:'Four', 5:'Five', 6:'Six', 7:'Seven', 8:'Eight', 9:'Nine', 10:'Ten'}
    return dict1to10[num]
}


// Convert 11-19 to a string representation
function teens(num){
    dict11to19 = {11:'Eleven', 12:'Twelve', 13:'Thirteen', 14:'Fourteen', 15:'Fifteen', 16:'Sixteen', 17:'Seventeen', 18:'eighteen', 19:'Nineteen'}
    return dict11to19[num]
}

// Convert 20-99 to a string representation
function tens(num){
    dict20to99 = {1: 'Ten', 2:'Twenty', 3:'Thirty', 4:'Forty', 5:'Fifty', 6:'Sixty', 7:'Seventy', 8:'Eighty', 9:'Ninety', 10:'Hundred'}
    return dict20to99[num]
}

// need to convert to use this which will require me to do a string len and offset to get the // (Floor) devidor
var dict10to100000 = {3:100, 4:1000, 5:10000, 6:100000 }
var dict10to100000Label = {3: 'Hundreds', 4: 'Thousands', 5: 'Thousands', 6: 'Hundred Thousand' }

// Needs work for compund ranges like hundres, thousands, etc...
function hundreds_to_hundred_thousand(num) {
    output = ''
    str_num = toString(num)
    str_len = str_num.length
    if(str_len >= 3) { // process numbers greater than 99
        floor = Math.floor(num/dict10to100000[str_len])
        output = dict10to100000Label[str_len]
    } else if (str_len < 3) {
        if (20 <= num && num <= 99)  {
            output += tens(num%10)
            num = num%10
        }
        if (num < 1) {
            //return format_out(orig_num, output)
            output += ' '
        }
        if (10 < num && num < 20) {
            output += teens(num)
        } else {
            output += ones(num)
        }   
    }
    return output
}



// Convert 100-999 to a string representation
function hundreds(num) {
    output = ''
    hundreds = Math.floor(num/100)
    output = ones(hundreds)
    output += " Hundred"
    return output
}


function thousands(num) {
    output = ''
    hundreds = Math.floor(num/1000)
    output = ones(hundreds)
    output += " Thousand"
    return output
}


function tensofthousands(num) {
    output = ''
    ten = Math.floor(num/10000)
    output = tens(ten)
    output += " Thousand"
    return output
}

function hundredsofthousands(num) {
    output = ''
    hundreds = Math.floor(num/100000)
    output = ones(hundreds)
    output += " Hundred Thousand"
    return output
}



function format_out(num, string) {
    return ("Number: " + num + " ---> Written Number: " + string)
}

// Converts numbers  from 0-999 to a string representation
function convert_number_phrase(num) {
    orig_num = num
    output = ''

    if (100000 <= num && num < 1000000) {
        output += hundredsofthousands(num)
        num = num%100000
        if (num < 1 ) { 
            return format_out(orig_num, output)
        }
        output += ' '
    }

    if (10000 <= num && num < 100000) {
        output += tensofthousands(num)
        num = num%10000
        if (num < 1) {
            return format_out(orig_num, output)
        }
        output += ' '
    }

    if (1000 <= num && num < 10000) {
        output += thousands(num)
        num = num%1000
        if (num < 1) {
            return format_out(orig_num, output)
        }
        output += ' '
    }

    if (100 <= num && num < 1000) {
        output += hundreds(num)
        num = num%100
        if (num < 1) {
            return format_out(orig_num, output)
        }
        output += ' '
    }

    if (20 <= num && num <= 99) {
        output += tens(Math.floor(num/10))
        num = num%10
        if (num < 1) {
            return format_out(orig_num, output)
        }
        output += ' '
    }
        
    if (10 < num && num < 20) {
        output += teens(num)
    } else {
        output += ones(num)
    } 
        
    return format_out(orig_num, output) 
}

