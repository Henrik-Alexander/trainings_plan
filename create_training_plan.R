### Create a training plan ---------------------------


## Functions ----------------------------------------

# Funciton to adjustt the current pace for the shorter distnace
adjust_current_pace <- function(pace, endurance_gap = distance - endurance) {
  pace + endurance_gap * 0.005 + endurance_gap ^2 * 0.005
}

## Set the basic paramters --------------------------

# Time
start_date <- as.Date("2024-07-14")
end_date <- as.Date("2024-10-31")

# Race target
distance <- 42.2
time <- 3.5 * 60
target_pace <- time / distance

# Current status
endurance <- 25
pace <- 4.40

# Estimate the time
training_period <- end_date - start_date
weeks <- as.numeric(training_period) / 7


### Adjust the current pace for the distance ---

# Estimate the adjusted current pace
distance - endurance

### Set the training plan ----------------------

# Endurance
endurance_increment <- (distance - endurance) / weeks

# Pace increment
pace_increment <- (target_pace - adjust_current_pace(pace)) / weeks


# Strength training
if (distance > 20) {
  strength_training <- 
  } else {
  strength_training <- 
}

# Flexibility training





### END ###########################################