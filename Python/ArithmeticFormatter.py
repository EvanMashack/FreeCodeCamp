# Assignment: https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/arithmetic-formatter
# Test Case is at bottom of ArithmeticFormatter.py

#function to return a line of a set number of the same character
def create_line(number, character):
  line = ""
  
  for i in range(number):
    line += character

  return line

#function to return math problems reformatted and optionally solved
def arithmetic_arranger(problems = [], solve = False): 
  #[Requirement 1]: Limit is 5 problems
  if len(problems) > 5:
    return "Error: Too many problems."

  #Variables to store the combined output
  resultsLine1 = ""
  resultsLine2 = ""
  resultsLine3 = ""
  resultsLine4 = ""
  results = ""
  index = 0
  
  for problem in problems:
    index += 1
    splitProblems = problem.split(" ")  
    operand1 = splitProblems[0]
    operator = splitProblems[1]
    operand2 = splitProblems[2]
    answer = 0
    resultLength = 0
    
    #[Requirement 2]: Only addition and subtration problems
    if operator != "+" and operator != "-":
      return "Error: Operator must be '+' or '-'."

    #[Requirement 4]: Operands can have a maximum of 4 digits
    if len(operand1) > 4 or len(operand2) > 4:
        return "Error: Numbers cannot be more than four digits."

    #Finding the max length of the 2 operands to use as a width for the problem
    if len(operand1) > len(operand2):
      resultLength = len(operand1) + 2
    else:
      resultLength = len(operand2) + 2

    #Reformating our results to be vertical. 
    resultsLine1 += operand1.rjust(resultLength)
    resultsLine2 += operator + operand2.rjust(resultLength - 1)
    resultsLine3 += create_line(resultLength, "-")
      
    #[Requirement 3]: Only whole number operands
    try:
      operand1 = int(operand1)
      operand2 = int(operand2)
    except:  
      return "Error: Numbers must only contain digits." 
    
    #Finding the answer       
    if solve:
      if operator == "+":
        answer = operand1 + operand2
      elif operator == "-":  
        answer = operand1 - operand2 
        
      resultsLine4 += str(answer).rjust(resultLength)

    #Adding spaces between problems if necessary
    if index < len(problems):
      resultsLine1 += create_line(4, " ")
      resultsLine2 += create_line(4, " ")
      resultsLine3 += create_line(4, " ")
      resultsLine4 += create_line(4, " ")
      
  results = resultsLine1 + "\n" + resultsLine2 + "\n" + resultsLine3 + "\n" + resultsLine4
  return results.rstrip() 
 
#Test case
#print(arithmetic_arranger(['3 + 855', '988 + 40'], True))
