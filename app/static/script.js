// Garlic Fries: Diana Akhmedova, Samantha Hua, Gitae Park, Vivian Teo
// SoftDev
// P01 -- NBA Love Story
// 2022-12-14
// time spent:  hrs

function give_item() {
    if (document.getElementById('item').checked) {
        // display item by making opacity 1    
        var correct = document.getElementById('display-item')
        correct.style.opacity = "1";

        // display the next step of the storyline, yes-no reaction
        var correct = document.getElementById('display-section-2')
        correct.style.opacity = "1";
    }
    else {
        var correct = document.getElementById('display-item')
        correct.style.opacity = "0";
    }
  }

  function display_yes_no() {
    if (document.getElementById('yes-no').checked) {
        var correct = document.getElementById('display-yes-no')
        correct.style.opacity = "1";
    }
    else {
        var correct = document.getElementById('display-yes-no')
        correct.style.opacity = "0";
    }
  }