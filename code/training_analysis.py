# Import packages
import functions
import os

# Apply the class -------------------------

# Set the path
path = "../data"
files = os.listdir(path)

# Load the data
training = training_report(f"{path}/{files[1]}")
training.clean_data()
training.summary()

## Plotting -------------------

# Plot the heart rate
training.plot_running(training.df["Avg HR"], "heart rate")

# Create a plot of the cadence
training.plot_running(y = training.df["Max Run Cadence"],
                      ylab = "Cadence (Steps/Minute)")

### End ###########################