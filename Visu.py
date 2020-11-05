import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Importing data from Excel and Coverting it to DataFrame
file = pd.ExcelFile(r'') #file directory
data = pd.read_excel(file, usecols=["countriesAndTerritories", "month", "cases"])
df = pd.DataFrame(data)

#Filtering The Data
file_xl = df.loc[df["countriesAndTerritories"] == "Saudi_Arabia"]

#Coverting it to Numpy array
np_mo = np.array(file_xl[["month"]])
np_ca = np.array(file_xl[["cases"]])

#Customizing the graph
plt.title("Saudi Arabia Covid cases: ")
plt.xlabel("Months")
plt.ylabel("Cases")
plt.plot(np_mo, np_ca)
plt.show()