import matplotlib.pyplot as plt
import pandas as pd

# Read the Excel data
df = pd.read_excel("Book2.xlsx")

# Create a list of the column names that contain the data to be plotted
columns = ["Precision", "Recall", "F1-Score"]
print(columns)
# Create a list of the colors to use for the lines
colors = ["red", "green", "blue", "blue"]
line_style = ["solid", 'dashed', 'dotted']
user = [4, 7, 18, 24, 33]
#
# # Plot the lines
for i, column in enumerate(columns):
    plt.plot(user, df[column],  linewidth=2, linestyle=line_style[i], color=colors[i])
#
# # Add a title to the plot
plt.title("Cluster based experiment")
#
# # Add a legend to the plot
plt.legend(columns)
#
# # Show the plot
plt.show()
