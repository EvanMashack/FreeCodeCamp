// Assignment: https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/javascript-algorithms-and-data-structures-projects/cash-register
// Test Case at bottom of OpenCashRegister.js

function openCashRegister(price, cash, cid) {
  const units = [.01, .05, .1, .25, 1, 5, 10, 20, 100]; 
  let changeArray = [
                      ["PENNY", 0],
                      ["NICKEL", 0], 
                      ["DIME", 0],
                      ["QUARTER", 0],
                      ["ONE", 0],
                      ["FIVE", 0],
                      ["TEN", 0],
                      ["TWENTY", 0],
                      ["ONE HUNDRED", 0] 
                     ]; 
  let leftInDrawer = 0;
  // Converting all units to whole numbers to avoid rounding errors
  let change = (cash - price) * 100;
  
  for(let i in units) {
    units[i] *= 100;
    cid[i][1] *= 100;
  }

  while(change > 0) {
    for(let i = units.length - 1; i >= 0; i--) { 
      // Take money from drawer if possible
      if(change >= units[i] && cid[i][1] > 0) {
        cid[i][1] -= units[i];
        changeArray[i][1] += units[i];
        change -= units[i]; 
        break;
      }
      // All units checked, insufficient funds to support change
      if(i == 0)
      {
        return {status: "INSUFFICIENT_FUNDS", change: []};
      }    
    }  
  } 

  // converting all units back to their original value
  for(let i in units) {
    changeArray[i][1] *= .01;
    leftInDrawer += cid[i][1];
  }

  if(leftInDrawer > 0)
  {
    return {status: "OPEN", change: changeArray.filter(element => element[1] > 0).reverse()};
  }
  // Include units with 0 as the total to display status;
  else 
  {
    return {status: "CLOSED", change: changeArray}; 
  }
} 

// Test Case
console.log(openCashRegister(3.26, 100, [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.1], ["QUARTER", 4.25], ["ONE", 90], ["FIVE", 55], ["TEN", 20], ["TWENTY", 60], ["ONE HUNDRED", 100]]));  
