# Assignment: https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/budget-app
# Test Case at the bottom of BugetCalculator.py

import math 

# Class to build a buget list
class Category:   
  def __init__(self, category):
    self.category = category
    self.ledger = []
    
  def __str__(self):
    spacing = 29
    # Category title centered in asterisks
    objectString = self.category[0: spacing].center(spacing + 1).replace(" ", "*") 
    # First 23 characters of the decriptions followed by the amount
    for i in range(len(self.ledger)):
      objectString += "\n" + self.ledger[i]["description"][0:23] + " " + str('%.2f' % self.ledger[i]["amount"])[0:7].rjust(spacing - len(self.ledger[i]["description"][0:23]))
    # Total for the category
    objectString += "\nTotal: " + str(self.get_balance())
    return objectString
    
  def deposit(self, amount, description = ""): 
    self.ledger.append({"amount": amount, "description": description}) 
    return True

  def withdraw(self, amount, description = ""):
    if not self.check_funds(amount):
      return False
    self.ledger.append({"amount": -amount, "description": description}) 
    return True 

  def get_balance(self):
    balance = 0
    for i in range(len(self.ledger)): 
      balance += self.ledger[i]["amount"]
    return balance

  def transfer(self, amount, other):
    if not self.withdraw(amount, "Transfer to " + other.category):
      return False
    other.deposit(amount, "Transfer from " + self.category)
    return True

  def check_funds(self, amount): 
    if amount > self.get_balance():
      return False
    return True
    
def create_spend_chart(categories):
  barChart = "Percentage spent by category" 
  percentages = balance_percentages(categories)
  percentage = 100
  
  # Appending the percentage label and possible category percentage if the bar should reach that high 
  while(percentage >= 0):
    barChart += "\n" + (str(percentage) + "|").rjust(4) + " "
    for i in range(len(percentages)):
      if percentages[i] >= percentage:
        barChart += "o  "
    percentage -= 10
    
  # Every category takes up 3 spaces plus the leading space after the label
  dashLength = (len(categories) * 3) + 1
  barChart += "\n" + ("-" * dashLength).rjust(4 + dashLength)  
  
  # Appending the category labels vertically : each category
  for i in range(max_category_length(categories)):
    barChart += "\n" + " ".rjust(5)  
    # each letter of the categories
    for j in range(len(categories)): 
      if i < len(categories[j].category):
        barChart += categories[j].category[i] + "  "
      else:
        barChart += "   "
  barChart = "Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  " 
  return barChart

# used in create_spend_chart to determine a percentage rounded to the nearest 10
def balance_percentages(categories):
  percentages = []
  totalBalance = 0
  for i in range(len(categories)):
    totalBalance += categories[i].get_balance()
  for i in range(len(categories)):
    percentage = int(round(categories[i].get_balance() / totalBalance, 1) * 100)  
    percentages.append(percentage)
  return percentages

# Used in create_spend_chart to print out category names vertically
def max_category_length(categories):
  maxLength = 0
  for i in range(len(categories)):
    if len(categories[i].category) > maxLength:
      maxLength = len(categories[i].category)
  return maxLength


# Test
""" 
food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")

food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")

food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99) 

print(food)
print("\n")
print(create_spend_chart([food, entertainment, business]))
""" 
