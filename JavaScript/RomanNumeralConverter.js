function convertToRoman(arabicNumeral) {
 // Both sets of numerals stored as objects in an array
 const numerals = [
                      {roman: "M", arabic: 1000},
                      {roman: "CM", arabic: 900},
                      {roman: "D", arabic: 500},
                      {roman: "CD", arabic: 400},
                      {roman: "C", arabic: 100},
                      {roman: "XC", arabic: 90},
                      {roman: "L", arabic: 50},
                      {roman: "XL", arabic: 40},
                      {roman: "X", arabic: 10},
                      {roman: "IX", arabic: 9},
                      {roman: "V", arabic: 5},
                      {roman: "IV", arabic: 4},
                      {roman: "I", arabic: 1},
                    ]

  // Empty array to store the converted value
  let romanNumeral = []; 

  // Internal conversion function to be called recursively
  function convertRecursively(arabicNumeral) {

    for(let i = 0; i < numerals.length; i++) {
      if(arabicNumeral >= numerals[i]["arabic"])
      {
        // The function will get called again if there are still numerals to convert
        arabicNumeral -= numerals[i]["arabic"];

        if(arabicNumeral > 0) {
          convertRecursively(arabicNumeral);
        }

        romanNumeral.unshift(numerals[i]["roman"]);
      
        return;
      }
    }
  } 

  convertRecursively(arabicNumeral); 

  return romanNumeral.join("");
}

console.log(convertToRoman(1603));
