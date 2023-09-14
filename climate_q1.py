import sqlite3
import matplotlib.pyplot as plt

# Connect to the SQLite database
conn = sqlite3.connect("climate.db")
cursor = conn.cursor()

# Execute an SQL query to fetch data
cursor.execute("SELECT Year,CO2,Temperature FROM climateData")

# Fetch all rows of data from the query result
rows = cursor.fetchall()

# Separate the data into lists
years = []
co2 = []
temp = []

for row in rows:
    years.append(row[0])
    co2.append(row[1])
    temp.append(row[2])

# Close the database connection
conn.close()

# Plot the data
plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--')
plt.title("Climate Data")
plt.ylabel("[CO2]")
plt.xlabel("Year (decade)")

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-')
plt.ylabel("Temp (C)")
plt.xlabel("Year (decade)")

plt.show()
plt.savefig("co2_temp_1.png")

