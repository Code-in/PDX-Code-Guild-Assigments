let app = new Vue({
    el: '#app',
    data: {
        leftval: '',
        rightval: '',
        operations: '',
        output: '0'
    },
    methods: {
        operatorClicked: function(operation) {
            if (this.operations === '')  {
                this.operations = operation
                this.output = this.leftval + " " + this.operations
            } else if (operation === '=' && this.rightval !== '' && this.leftval !== '' && this.operations !== '') { // // sum of the left and right values based onthe opperan
                this.leftval = this.calculate(this.leftval, this.rightval, this.operations)
                this.leftval = this.leftval.toString()
                console.log("operatorClicked: leftVal [" + this.leftval + "]")
                console.log("operatorClicked [" + this.leftval + "] [" + this.operations + "] [" + this.rightval + "]")
                this.printOutput(this.leftval)
                this.rightval = ''
                this.operations = ''
            }
        },
        valueClicked: function(value) {
            if (this.operations === '' && this.rightval === '')  {
                this.leftval += value
                this.printOutput(this.leftval)
            } else if (this.operations !== '' && this.lefttval !== '') {
                this.rightval += value
                this.output = this.leftval + " " + this.operations + " " + this.rightval
            } else {
                console.log("valueClicked has an issue")
                TouchEvent.output = "Error: valueClicked"
            }
        },
        specialOperatorClicked: function(operation) {
            if (operation === 'Æ') {  // Clean All values and opeartions
                this.rightval = ''
                this.leftval = ''
                this.operations = ''
                this.printOutput('0')
            } else if (operation === '%' && this.rightval !== '' && this.leftval !== '' && this.operations !== '') { // Convert the right value to percentage
                this.rightval = this.convertToFloatOrInt(this.rightval /= 100).toString()
                this.printOutput(this.rightval)
            }  else if (operation === '%' && this.rightval === '' && this.leftval !== '' && this.operations === '') { // Convert the left value to percentage
                this.leftval = this.convertToFloatOrInt(this.leftval /= 100).toString()
                this.printOutput(this.leftval)
            } else if (operation === '±' && this.rightval !== '' && this.leftval !== '' && this.operations !== '') { // Change the sign of the right value
                this.rightval = "-" + this.rightval
                this.printOutput(this.rightval)
            }  else if (operation === '±' && this.rightval === '' && this.leftval !== '' && this.operations === '') { // Change the sign of the left value
                this.leftval = "-" + this.leftval
                this.printOutput(this.leftval)
            } else {
                console.log("specialOperatorClicked has an issue")
                TouchEvent.output = "Error: specialOperatorClicked"
            }
        },
        calculate: function(leftval, rightval, operations) {

            console.log("calculate [" + typeof(leftval) + "] [" + typeof(operations) + "] [" + typeof(rightval) + "]")
            console.log("calculate [left: " + leftval + "] [operator: " + operations + "] [right: " + rightval + "]")

            //leftval = this.convertToFloatOrInt(leftval)
            //rightval = this.convertToFloatOrInt(rightval)
            if(typeof(stringVal) === "string") {
                leftval = parseFloat(leftval).toFixed(2)
            }
            if(typeof(stringVal) === "string") {
                rightval = parseFloat(rightval).toFixed(2)
            }
            if(operations === '+') {
                console.log("calculate [" + typeof(leftval) + "] [" + typeof(operations) + "] [" + typeof(rightval) + "]")
                console.log("calculate [left: " + leftval + "] [operator: " + operations + "] [right: " + rightval + "]")
                return  (leftval + rightval)
            } else if(operations === '-') {
                return  (leftval - rightval)
            } else if(operations === 'x') {
                return  (leftval * rightval)
            } else if(operations === '÷') {
                return  (leftval / rightval)
            } else {
                return "Error: calculate"
            }
        },
        convertToFloatOrInt: function(stringVal) {
            console.log(typeof(stringVal))
            if(typeof(stringVal) !== "string") {
                stringVal = stringVal.toString()
            }
            console.log("IN - convertToFloatOrInt [" + typeof(stringVal) + "]")
            if (stringVal.includes('.')) {
                stringVal = parseFloat(stringVal).toFixed(2)  // Check to see if this returns a string for my knowledge!!!!
            } else {
                stringVal = parseInt(stringVal)
            }
            console.log("OUT - convertToFloatOrInt [" + (typeof stringVal) + "]")
            return stringVal
        },

        printOutput: function(value) {
            //if(typeof(value) === "string") {
            //    value = this.convertToFloatOrInt(value)
            //}
            this.output = value.toString()
        }
    }
})


