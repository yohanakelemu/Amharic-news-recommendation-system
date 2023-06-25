import matplotlib.pyplot as plt
import pandas as pd

# Read the Excel data
df = pd.read_excel("Book1.xlsx")

# Create a list of the column names that contain the data to be plotted
columns = ["Precision", "Recall", "F1-Score"]
print(columns)
# Create a list of the colors to use for the lines
colors = ["red", "green", "blue", "blue"]
line_style = ["solid", 'dashed', 'dotted']
user = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
#
# # Plot the lines
for i, column in enumerate(columns):
    plt.plot(user, df[column], linewidth=2, linestyle=line_style[i], color=colors[i])
#
# # Add a title to the plot
plt.title("Single user based experiment")
#
# # Add a legend to the plot
plt.legend(columns)
#
# # Show the plot
plt.show()
