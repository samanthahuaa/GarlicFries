// Garlic Fries: Diana Akhmedova, Samantha Hua, Gitae Park, Vivian Teo
// SoftDev
// P01 -- NBA Love Story
// 2022-12-21
// time spent:  hrs

function give_item() {
    // display item by making opacity 1    
    var correct = document.getElementById('display-item')
    correct.style.display = "inline";

    // display the next step of the storyline, yes-no reaction
    var correct = document.getElementById('display-section-2')
    correct.style.display = "inline";

    // change progress bar
    progressBar = document.getElementById("bar")
    progressBar.innerHTML = "33/100"
    progressBar.style.width = "33%";

    // disable button
    button = document.getElementById("item-button")
    button.disabled = true;
    button.style.background = "#662f2c";
  }

  function display_yes_no() {
    var correct = document.getElementById('display-yes-no')
    correct.style.display = "inline";

    // display the next step of the storyline, love-calc, show compatability
    var correct = document.getElementById('display-section-3')
    correct.style.display = "inline";

    // change progress bar
    progressBar = document.getElementById("bar")
    progressBar.innerHTML = "66/100"
    progressBar.style.width = "66%";

    // disable button
    button = document.getElementById("yes-no-button")
    button.disabled = true;
    button.style.background = "#662f2c";
  }

  function display_love_calc() {
    var correct = document.getElementById('display-love-calc')
    correct.style.display = "inline";

    // display the next step of the storyline, date schedule
    var correct = document.getElementById('display-section-4')
    correct.style.display = "inline";

    // display summary
    var correct = document.getElementById('display-summary')
    correct.style.display = "inline";     
    
    // change progress bar
    progressBar = document.getElementById("bar")
    progressBar.innerHTML = "100/100"    
    progressBar.style.width = "100%";

    // disable button
    button = document.getElementById("love-calc-button")
    button.disabled = true;
    button.style.background = "#662f2c";
  }