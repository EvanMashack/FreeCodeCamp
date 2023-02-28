// Assignment: https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/javascript-algorithms-and-data-structures-projects/palindrome-checker
// Test Case at the bottom of PalindromeChecker.js

function palindrome(str) {
    // Removing all non-alphanumeric characters and normalizing the case;
    const regex = /[^A-Za-z0-9]/g
    let scrubbedStr = str.replace(regex, "").toLowerCase(); 

    // reversing the string for palindrome check
    let reversedStr = scrubbedStr.split("").reverse().join(""); 
  
    return (scrubbedStr == reversedStr);
  }
  
  // Test Case
  //console.log(palindrome("A man, a plan, a canal. Panama"));
