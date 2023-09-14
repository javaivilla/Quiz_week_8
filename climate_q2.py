import matplotlib.pyplot as plt
import pandas as pd

# Load data from the CSV file
data = pd.read_csv("climate.csv")

# Extract columns from the loaded data
years = data["Year"]
co2 = data["CO2"]
temp = data["Temperature"]

# Create a figure with subplots
plt.figure(figsize=(10, 6))

# Plot CO2 data
plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

# Plot Temperature data
plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 

# Display the figure
plt.tight_layout()
plt.show()

# Save the figure as an image file
plt.savefig("co2_temp_2.png")

