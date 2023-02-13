function palindrome(str) {
    // Removing all non-alphanumeric characters and normalizing the case;
    const regex = /[^A-Za-z0-9]/g
    let scrubbedStr = str.replace(regex, "").toLowerCase(); 

    // reversing the string for palindrome check
    let reversedStr = scrubbedStr.split("").reverse().join(""); 
  
    return (scrubbedStr == reversedStr);
  }
  
  console.log(palindrome("A man, a plan, a canal. Panama"));
