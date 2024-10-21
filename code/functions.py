### Packages
import pandas as pd
import matplotlib.pyplot as plt

## Helper functions ----------------------


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

## Training class -------------------------

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
        self.df["pace"] = clean_pace(self.df["Avg Pace"]).apply(mile_km_pace)
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