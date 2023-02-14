function rot13(encodedStr) {
  // Uppercase letters are required so this cast is an error precaution
  encodedStr = encodedStr.toUpperCase().split("");
  let decodedStr = []; 

  function decode(asciiDecimal) {
    // Only letter characters are being decoded
    if(asciiDecimal >= 65 && asciiDecimal <= 90) {
      if(asciiDecimal + 13 > 90) { 
        // Z is 90 so any remainder after needs to be added to A at 65
        return (65 + ((asciiDecimal + 13) % 91));
      }
      else {
        return asciiDecimal + 13;
      }
    }
    else {
      return asciiDecimal;
    }
  }

  // Applying our decode function on the encodedStr and storing the result as an aray of ASCII Decimals 
  for(let i in encodedStr) { 
    decodedStr.push(decode(encodedStr[i].charCodeAt(0)));
  }  
  // The array needs to be converted back into a string of characters
  return String.fromCharCode(...decodedStr);
}

console.log(rot13("GUR DHVPX OEBJA SBK WHZCF BIRE GUR YNML QBT.")); 
  
