

let app = new Vue({
    el: '#app',
    data: {
        number_to_convert: 0,
        number_to_phrase: ''
    },
    methods: {
        convertToPhrase: function() {
            this.number_to_phrase = convert_number_phrase(this.number_to_convert)
        },
    }
})

// Convert 1-10 to a string representation
function ones(num){
    let dict1to10 = {0:'Zero', 1:'One', 2:'Two', 3:'Three', 4:'Four', 5:'Five', 6:'Six', 7:'Seven', 8:'Eight', 9:'Nine', 10:'Ten'}
    return dict1to10[num]
}


// Convert 11-19 to a string representation
function teens(num){
    let dict11to19 = {11:'Eleven', 12:'Twelve', 13:'Thirteen', 14:'Fourteen', 15:'Fifteen', 16:'Sixteen', 17:'Seventeen', 18:'eighteen', 19:'Nineteen'}
    return dict11to19[num]
}

// Convert 20-99 to a string representation
function tens(num){
    let dict20to99 = {1: 'Ten', 2:'Twenty', 3:'Thirty', 4:'Forty', 5:'Fifty', 6:'Sixty', 7:'Seventy', 8:'Eighty', 9:'Ninety', 10:'Hundred'}
    return dict20to99[num]
}

function convert_to_phrase(num, divisor, in_output ) {
    let output = in_output
    let tens_place = Math.floor(num/divisor)
    if(divisor === 100000) {
        output += ones(tens_place)
        output += " Hundred Thousand"
        num = num%100000
    } else if (divisor === 10000) {
        output += tens(tens_place)
        output += " Thousand"
        num = num%10000
    } else if (divisor === 1000) {
        output += ones(tens_place)
        output += " Thousand"
        num = num%1000
    } else if (divisor === 100) {
        output += ones(tens_place)
        output += " Hundred"
        num = num%100
    }  
    return [num, output]
}

function format_out(num, string) {
    return string //("Number: " + num + " ---> Written Number: " + string)
}

// function get_divsor(num) {
//     if (num == 0) return [0];
//     var arr = [];
//     var i = 1;
  
//     while (num > 0) {
//       arr.unshift((num % 10) * i);
//       num = Math.floor(num / 10);
//       i *= 10
//     }
//     return arr[0];
//   }

function get_divsor(num) {
    console.log(num)
    let num_len = num.toString().length
    let str = "1".concat("0".repeat(num_len - 1))
    console.log(str)
    return parseInt(str)
}

// Converts numbers  from 0-999 to a string representation
function convert_number_phrase(in_num) {
    let output = ''
    let num = parseInt(in_num)

    while (100 <= num && num < 1000000) {
        let divsor = get_divsor(num)
        tmparr = convert_to_phrase(num, divsor, output)
        num = tmparr[0]
        output = tmparr[1]
        if (num < 1 ) { 
            return format_out(in_num, output)
        }
        output += ' '
    }

    if (20 <= num && num <= 99) {
        output += tens(Math.floor(num/10))
        num = num%10
        if (num < 1) {
            return format_out(in_num, output)
        }
        output += ' '
    }
        
    if (10 < num && num < 20) {
        output += teens(num)
    } else {
        output += ones(num)
    } 
        
    return format_out(in_num, output) 
}