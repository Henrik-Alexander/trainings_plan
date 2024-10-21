# Import packages
import pandas as pd
import matplotlib.pyplot as plt
import os

## Functions -------------------


# Basic plotting function
def plot_running(y, ylab):
    fig, ax = plt.subplots()
    ax.step(df.kilometer.cumsum(), y)
    ax.hlines(y = y.mean(), 
            xmin = df.kilometer.min(),
            xmax = mile_km(total.Distance),
            color = "black",
            alpha = 0.5)
    plt.xlabel("Distance (km)")
    plt.ylabel(ylab)
    plt.show()
    return plt

# Clean the pace
def clean_pace(pace):
    pace = pace.str.replace(":", ".")
    return pd.to_numeric(pace)

# Translate mile to kilometer
def mile_km(mile):
    return mile / 0.62

    
# Translate minutes/mile to minutes/kilometer
def mile_km_pace(pace):
    return pace * 0.62


# Function to summarize the session
# Create a class object that summarizes the training session
# Create the most important plots
class training_report:
    def __init__(self, file_path):
        """Initialize the data"""
        self.df = pd.read_csv(file_path)
  
    # Create the kilometer column
    def clean_data(self):
        self.df["kilometer"] = self.df["Distance"].apply(mile_km)
        self.df["pace"] = clean_pace(self.df["Avg Pace"])
        self.total = self.df[self.df["Laps"] == "Summary"]
        self.df = self.df[self.df["Laps"] != "Summary"]
        
    # Return the summary report
    def summary(self):
        self.report = {}
        self.report["Distance"] = self.total["kilometer"]
        self.report["pace"] = self.df["pace"].describe()
        self.report["heart rate"] = self.df["Avg HR"].describe()
        self.report["cadence"] = self.df["Max Run Cadence"].describe()
        print(self.report)
    
    # Plot the data
    def plot_running(self, y, ylab):
        """Plot of a running variable running"""
        fig, ax = plt.subplots()
        ax.step(self.df.kilometer.cumsum(), y)
        ax.hlines(y = y.mean(), 
                xmin = df.kilometer.min(),
                xmax = mile_km(total.Distance),
                color = "black",
                alpha = 0.5)
        plt.xlabel("Distance (km)")
        plt.ylabel(ylab)
        plt.show()
        return plt
        

# Load the data
training = training_report("../data/activity_17330403407.csv")
training.clean_data()
training.summary()
training.plot_running(training.df["Avg HR"], "heart rate")


# Apply the class
today = training_report()

today = training_report(df)
today = training_report.from_csv("../data/activity_17330403407.csv")


## Data preparation ------------

# Load the data
file = os.listdir("data")
df = pd.read_csv("data/" + file[0])

# Split the kilometers from total
total = df[df["Laps"] == "Summary"]
df = df[df["Laps"] != "Summary"]

## Summary statistics -----------
#
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