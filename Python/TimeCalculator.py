# Function to return the time, day of the week and number of days passed after start time.
def add_time(start, duration, day = ""):
  weekdays = ["", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
  weekday = ""
  dayIndex = 0

  # We're only concerned with valid weekday values.
  try:
    dayIndex = weekdays.index(day.casefold().capitalize())
  except:
    dayIndex = 0

  # Converting the start and duration time to minutes to make it easier to work with
  sTime = start.split(" ")[0]
  sHours = int(sTime.split(":")[0])
  sMinutes = int(sTime.split(":")[1])
  
  dTime = duration.split(" ")[0]
  dHours = int(dTime.split(":")[0])
  dMinutes = int(dTime.split(":")[1])

  sAsMinutes = (sHours * 60) + sMinutes
  dAsMinutes = (dHours * 60) + dMinutes

  # Setting our initial meridian bit
  afterNoon = False
  meridian = " AM"
  
  if start.split(" ")[1] == "PM":
    afterNoon = True

  days = 0

  #
  # Calculation section
  #

  # Hours are converted to minutes. 12h = 720m, 24h = 1440m
  while dAsMinutes >= 720:
    # 24 hour time intervals do not effect the time but days need to be calculated
    if dAsMinutes >= 1440:
      days = int(dAsMinutes/1440)
      dAsMinutes -= days * 1440

    # 12 hour time intervals do not effect the time but does flip the meridian bit
    if dAsMinutes >= 720:
      dAsMinutes -= 720
      afterNoon = not afterNoon

  # Durations less than 12 hours effect the time
  if dAsMinutes > 0:
    # if we're crossing over a merdian the bit needs to be flipped
    if sAsMinutes < 720 and sAsMinutes + dAsMinutes >= 720:
      afterNoon = not afterNoon

      # if the merdian is now AM a day has passed
      if not afterNoon:
        days += 1
        
    # Add what's left of the duration to the start time     
    sAsMinutes += dAsMinutes

    # 13:00 becomes 1:00 and so on
    if sAsMinutes > 780: 
      sAsMinutes -= 720  

  #
  # Results formatting section
  #
      
  if afterNoon:
    meridian = " PM"

  rHours = str(int(sAsMinutes/60))
  rMinutes = str(sAsMinutes % 60)

  # Minutes should always be 2 digits
  if len(rMinutes) == 1:
    rMinutes = "0" + rMinutes

  rDays = "" 

  # Finding the weekday after the duration has passed
  if dayIndex > 0: 
    # 7 day intervals do not effect the weekday
    dayIndex += int(days % 7)
    # Starting back at Monday after Friday
    if dayIndex > 7:
      dayIndex -= 7    
    rDays = ", " + weekdays[dayIndex]
  
  if days > 1:
    rDays += " (" + str(days) + " days later)"
  elif days == 1:
    rDays += " (next day)"
    
  return rHours + ":" + rMinutes + meridian + rDays

# Test Case
#print(add_time("11:59 AM", "192:01", "Friday"))
