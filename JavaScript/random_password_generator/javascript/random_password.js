

// Create the character pool for the random generation of passwords
const uppercase_letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
const lowercase_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
const number_letters = ['0','1','2','3','4','5','6','7','8','9']
const special_letters = ['!','"','#','$','%','&','\'','(',')','*','+',',','-','.','/',':',';','<','=','>','?','@','[','\\',']','^','_','`','{','|','}','~']
const chars = lowercase_letters + uppercase_letters + number_letters + special_letters


// Select the generate passord button and add a Event listener for click actions on the button
let password_generator = document.querySelector("#generate_password_button");
console.log("Got Button: " + password_generator)
password_generator.addEventListener("click", function() {
    main()
});

// Create the random password per the length requested
function create_random_password(password_len, character_set) {
    let pwd = []
    for (x = 0; x < password_len; x++) {
        rand = Math.floor( Math.random() * character_set.length );
        pwd.push(character_set[rand])
    }
    return pwd
}

// Function - to shuffle and array
function shuffle(parray) {
    var cindex = parray.length
    var tchar
    var rindex;

    while (cindex) {
        // pick a random index
        rindex = Math.floor(Math.random() * cindex--);

        // swap elements
        tchar = parray[cindex];
        parray[cindex] = parray[rindex];
        parray[rindex] = tchar;
    }
    return parray;
}

// Function - runtime function to take users input to generate a password
function main() {
    settings = {}
    // find out how many lowercase, uppercase, digits and special characters they want in custom generate password
    settings['lower'] = document.querySelector("#lowercase_characters").value
    settings['upper'] = document.querySelector("#uppercase_characters").value
    settings['numbers'] = document.querySelector("#number_characters").value
    settings['special'] = document.querySelector("#special_characters").value
    
    var lpwd = create_random_password(settings['lower'], lowercase_letters)
    var upwd = create_random_password(settings['upper'], uppercase_letters)
    var npwd = create_random_password(settings['numbers'], number_letters)
    var spwd = create_random_password(settings['special'], special_letters)
    var pwd_array = lpwd.concat(upwd , npwd, spwd)
    var rand_pwd_array = shuffle(pwd_array)

    var password = ""
    for (let i in rand_pwd_array) {
        password += rand_pwd_array[i]
    }

    console.log("New random password: " + password)
    document.querySelector("#password_output").innerText = password
}

