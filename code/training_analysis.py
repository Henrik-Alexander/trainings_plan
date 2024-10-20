# Import packages
import pandas as pd
import matplotlib.pyplot as plt
import os

## Functions -------------------


# Translate mile to kilometer
def mile_km(mile):
    return mile / 0.62

# Clean the pace
def clean_pace(pace):
    pace = pace.str.replace(":", ".")
    return pd.to_numeric(pace)

# Translate minutes/mile to minutes/kilometer
def mile_km_pace(pace):
    return pace * 0.62

# Basic plotting function
def plot_running(y, ylab):
    fig, ax = plt.subplots()
    ax.step(df.kilometer.cumsum(), y)
    ax.hlines(y = y.mean(), 
            xmin = df.kilometer.min(),
            xmax = mile_km(total.Distance),
            color = "black",
            alpha = 0.5)
    ax.xlabel("Distance (km)")
    ax.ylabel(ylab)
    ax.show()
    return ax

# Function to summarize the session
# Create a class object that summarizes the training session
# Create the most important plots
#class training_report():
    

    
    


## Data preparation ------------

# Load the data
file = os.listdir("data")
df = pd.read_csv("data/" + file[0])

# Create the kilometer column
df.kilometer = df["Distance"].apply(mile_km)

# Clean the pace vector
df["pace"] = clean_pace(df["Avg Pace"])

# Split the kilometers from total
total = df[df["Laps"] == "Summary"]
df = df[df["Laps"] != "Summary"]

## Summary statistics -----------

# Summarise the distance
mile_km(total.Distance)

# Summarise the kilometer pace
df.pace = df["pace"].apply(mile_km_pace)

# Summarise cadence, heart rate and pace
df[["pace", "Max Run Cadence", "Avg HR"]].describe()


## Plotting -------------------

# Create a plot of the cadence
plot_running(y = df["Max Run Cadence"],
             ylab = "Distance (Steps/Minute)")

# Plot the heartrate
plot_running(y = df["Avg HR"],
             ylab = "Average Heart Rate")

### End ###########################