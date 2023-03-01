# Assignment: https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/probability-calculator
# Test Case at bottom of ProbabilityCalculator.py
import copy
import random 

class Hat:
  def __init__(self, **balls): 
    self.contents = []
    # Converting dictionary color count to list of individual colors
    for color in balls.keys():
      for i in range(balls.get(color)):
        self.contents.append(color) 

  def __str__(self):
    return str(self.contents)

  def draw(self, draws):
    # Can't draw more than we have
    if draws > len(self.contents):
      return self.contents
    hat = copy.deepcopy(self.contents)
    hand = []
    # Once a ball is drawn it's out of the hat
    for i in range(draws):
      j = random.randint(0, len(hat) - 1)
      ball = hat.pop(j)
      hand.append(ball)
    return hand
    
# Returns the probability of drawing your prediction
def experiment(hat, prediction, draws, attempts):  
  m = 0
  n = attempts
  # Attempting specified number of times
  for i in range(attempts):
    hand = hat.draw(draws)
    handDict = {}
    colorPredicted = 0
    # Converting list to dictionary to keep count value for key color
    for color in hand:
      amount = handDict.get(color)
      if amount is None:
        amount = 0
      handDict.update({color: amount + 1})
    # Comparing what's in our hand to what we predicted
    for color in prediction:
      amount = handDict.get(color)
      if amount is None:
        amount = 0
      if amount >= prediction.get(color):
        colorPredicted += 1
      else:
        # If we're wrong about one color we're bailing out
        break
    # if we're right about all colors it's a win
    if colorPredicted == len(prediction):
      m += 1;
  if m > 0:
    return m / n
  else:
    # Avoiding nasty divide by 0 errors
    return 0

# Test Case
"""
hat1 = Hat(blue=3,red=2,green=6)
print(experiment(hat1, {"blue":2,"green":1}, 4, 2))
"""
