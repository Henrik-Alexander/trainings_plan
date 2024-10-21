# Import packages
import functions
import os

# Apply the class -------------------------

# Load the data
training = training_report("../data/activity_17330403407.csv")
training.clean_data()
training.summary()

## Plotting -------------------

# Plot the heart rate
training.plot_running(training.df["Avg HR"], "heart rate")

# Create a plot of the cadence
training.plot_running(y = training.df["Max Run Cadence"],
                      ylab = "Cadence (Steps/Minute)")

### End ###########################