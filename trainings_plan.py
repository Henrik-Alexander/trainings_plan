# Import packages
import numpy as np
import matplotlib.pyplot as plt
import datetime as date

# Functions --------------------------

# Function to adjust the current pace for the shorter distance
def adjust_current_pace(pace, endurance_gap):
  return pace + endurance_gap * 0.005 + endurance_gap**2 * 0.005



# Set the basic parameters ---------------

# Time
start_date = date.datetime(year=2024, month=7, day=14)
end_date = date.datetime(year=2024, month=10, day=31)

# Race targets
distance = 42.2
time = 3.5 * 60
target_pace = time / distance

# Current status
endurance = 25
pace = 4.4

# Estimate the time
training_period = end_date - start_date
weeks = training_period.days // 7

### Adjust the current pace for the distance
distance-endurance

### Set the trainings plan -----------------

# Endurance
endurance_increment = (distance - endurance) / weeks
pace_increment = (target_pace - adjust_current_pace(pace, distance-endurance)) / weeks

# Strength training
if distance > 20:
  strength_training = 2
else:
  strength_training = 0
  
# Flexibility training



### END #################################
