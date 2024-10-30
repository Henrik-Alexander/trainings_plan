# Import packages
import numpy as np
import matplotlib.pyplot as plt
import datetime as date


# Functions --------------------------

class Training:
      def __init__(self, distance, pace, sessions):
           self.distance = distance
           self.pace = pace 
           self.sessions = sessions
      
      def create_period(self, race_year, race_month, race_day):
          self.today = date.date.today()
          self.raceday = date.date(race_year, race_month, race_day)
          self.duration = date.timedelta(self.raceday - self.today)
          if self.duration < 0:
                 raise ValueError("The race day must be in the future!")
               
      def create_training(self):
            self.schedule = []
            if self.distance > 10:
                  self.schedule.append("longrun")
            if self.pace < 5:
                  self.schedule.append("intervals")
            if self.sessions > 3:
                  self.schedule.append("strength")
            if len(self.schedule) < self.sessions:
              for i in 1:(len(self.schedule) - self.sessions):
                    self.schedule.append("normal run")      
            
           

marathon = trainings_plan(41, 4.5, 5)
marathon.create_period(year = 2024,
                       month = 10,
                       day = 28)

marathon.duration()
  
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


### Create the plan ----------------------

week = 8

def Training(week):

      # Set the endurance training
      distance_training = endurance + week * endurance_increment
      distance_speed_training = target_pace
      duration_distance_training = distance_training * target_pace
      
      # Additional endurance training
      additional_running_distance = week/weeks * 1/2 * distance
      additional_running_pace = target_pace * (weeks - week) / weeks 
      
      
      # Strength training
      
      # 
      




### END #################################
