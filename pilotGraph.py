import matplotlib.pyplot as plt

precision_ex1 = [0.740741, 0.787037, 0.777778, 0.787037, 0.787037, 0.731481, 0.648148, 0.583333, 0.481481, 0.611111,
                 0.62963, 0.564815, 0.62037, 0.601852, 0.537037, 0.57653]
recall_ex1 = [0.40404, 0.429293, 0.424242, 0.429293, 0.425, 0.39899, 0.443038, 0.398734, 0.396947, 0.420382, 0.427673,
              0.388535, 0.421384, 0.414013, 0.367089, 0.605263]
fscore_ex1 = [0.522876, 0.555556, 0.54902, 0.555556, 0.551948, 0.51634, 0.526316, 0.473684, 0.435146, 0.498113,
              0.509363, 0.460377, 0.501873, 0.490566, 0.43609, 0.754098]
user_ex1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
# Create a figure and a subplot
fig, ax = plt.subplots()

# Plot the precision values on the x-axis and the recall values on the y-axis
ax.plot(user_ex1, precision_ex1, linewidth=5, linestyle='solid', label='Precision')
ax.plot(user_ex1, recall_ex1, linewidth=5, linestyle='dashed', label='Recall')
ax.plot(user_ex1, fscore_ex1, linewidth=5, linestyle='dotted', label='F-Score')

# Add a title and labels to the axes
ax.set_title("Individual user based experiment")
# ax.set_xlabel("users")
# ax.set_ylabel("Recall")
ax.legend()
plt.show()

# Save the figure
plt.savefig("precision_recall.png")
