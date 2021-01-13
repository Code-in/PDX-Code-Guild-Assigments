

// Data for the options
const computer_choices = ['r','p','s','v','l']
const options = {'r':'Rock','p':'Paper','s':'Scissors','v':'Vulcan','l':'Lizard'}

/* Note there's only 3 options 
 0 - means they tied
 1 - means computer won
 2 - means player 1 wins
*/
const wins = {'rr':0, 'rs':1, 'rp':2, 'rv':2, 'rl':1, 
        'ss':0, 'sr':2, 'sp':1, 'sv':2, 'sl':1, 
        'pp':0, 'ps':2, 'pr':1, 'pv':1, 'pl':2, 
        'vv':0, 'vr':1, 'vp':2, 'vs':1, 'vl':2, 
        'll':0, 'lr':2, 'lp':1, 'ls':2, 'lv':1}

// main function for running the game logic      
function main(user_selection) {
    console.log("User selected: " + user_selection);
    computer_selection = askComputerForChoice()
    console.log("Computers selected: " + computer_selection);
    outcome = whoWon(computer_selection, user_selection)
    displayOutcome(outcome, computer_selection, user_selection)
}

// This will display text and graphic based on the winner, loser or tie
function displayOutcome(outcome, computer_selection, user_selection) {
    var winner = document.getElementById("winner_container");
    var loser = document.getElementById("loser_container");
    var tie = document.getElementById("tie_container");
    var description = document.getElementById("description_container");
    
    description.innerText = "You selected: " + options[user_selection] + ", the Computer selected: "  + options[computer_selection]
    if (outcome == 1) {
        winner.style.display = "none";
        loser.style.display = "block";
        tie.style.display = "none";
    } else if (outcome == 2) {
        winner.style.display = "block";
        loser.style.display = "none";
        tie.style.display = "none";
    } else {
        winner.style.display = "none";
        loser.style.display = "none";
        tie.style.display = "block";
    }
}

// Make a random selection of the options for the computer
function askComputerForChoice() {
    rand = Math.floor( Math.random() * computer_choices.length );
    return computer_choices[rand]
}

// Determine if the computer or you won based on selections
function whoWon(computer, player) {
    return wins[computer + player]
}
    
// Select the generate passord button and add a Event listener for click actions on the button
let buttonArray = document.querySelectorAll(".action_button");
for (button of buttonArray) {
    console.log(button)
    button.addEventListener("click", function() {
        console.log(button.dataset['character'])
        main(button.dataset['character'])
    });
}