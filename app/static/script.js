// Garlic Fries: Diana Akhmedova, Samantha Hua, Gitae Park, Vivian Teo
// SoftDev
// P01 -- NBA Love Story
// 2022-12-14
// time spent:  hrs

function give_item() {
    if (document.getElementById('item').checked) {
        // display item by making opacity 1    
        var correct = document.getElementById('display-item')
        correct.style.display = "inline";

        // display the next step of the storyline, yes-no reaction
        var correct = document.getElementById('display-section-2')
        correct.style.display = "inline";
    }
    else {
        var correct = document.getElementById('display-item')
        correct.style.display = "none";
    }
  }

  function display_yes_no() {
    if (document.getElementById('yes-no').checked) {
        var correct = document.getElementById('display-yes-no')
        correct.style.display = "inline";

        // display the next step of the storyline, love-calc, show compatability
        var correct = document.getElementById('display-section-3')
        correct.style.display = "inline";
    }
    else {
        var correct = document.getElementById('display-yes-no')
        correct.style.display = "none";
    }
  }

  function display_love_calc() {
    if (document.getElementById('love-calc').checked) {
        var correct = document.getElementById('display-love-calc')
        correct.style.display = "inline";

        // display the next step of the storyline, date schedule
        var correct = document.getElementById('display-section-4')
        correct.style.display = "inline";

        //display summary
        var correct = document.getElementById('display-summary')
        correct.style.display = "inline";        
    }
    else {
        var correct = document.getElementById('display-love-calc')
        correct.style.display = "none";
    }
  }