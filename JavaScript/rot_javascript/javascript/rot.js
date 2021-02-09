
// Select the generate passord button and add a Event listener for click actions on the button
const alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~0123456789 \t\n'
const alphabet_len = alphabet.length
var rotOffSet = Math.floor(alphabet_len/2)
var rotNegOffSet = -Math.floor(alphabet_len/2)
let encode_button = document.querySelector(".action_button")
console.log(encode_button)
encode_button.addEventListener("click", function(event) {
    let test_to_encode = document.querySelector(".test_to_encode")
    console.log(test_to_encode.value)
    encoded = rot(test_to_encode.value, rotOffSet)
    validated = rot(encoded, rotNegOffSet)
    document.querySelector(".encoded_container").innerHTML = "<p> Encoded: " + encoded + "</p>"
    document.querySelector(".validated_container").innerHTML = "<p> Validated: " + validated + "</p>"
})

// ROT encoder with a larger character set which supports all ASCII characters and punctation
function rot(text, offset) {

    
    offset = parseInt(offset)
    // Compenstate for large negative numbers
    if (offset < (-1 * alphabet_len)) {
        offset = offset * -1
    }

    if (offset < 0) { // Compenstate for negative numbers
        offset += alphabet_len
    } else if (offset > alphabet_len) { // Compenstate for large numbers
        offset %= alphabet_len
    }

    console.log("Offset: " + offset)
    let output = ''
    for (let i=0; i<text.length; i++) {
        let char = text[i]
        console.log("char: " + char)
        let alphabet_index = alphabet.indexOf(char)
        console.log("index of char: " + alphabet_index)
        if (alphabet_index == -1) {
            output += char
        } else {
            alphabet_index += offset
            console.log("alphabet_index: " + alphabet_index)
            alphabet_index %= alphabet_len
            console.log("alphabet_index after mod: " + alphabet_index)
            output += alphabet[alphabet_index]
        }
    }
    console.log("Output: " + output)
    return output
}