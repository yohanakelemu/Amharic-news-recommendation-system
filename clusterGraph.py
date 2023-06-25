import matplotlib.pyplot as plt

precision_ex1 = [0.967664, 0.914524, 0.967664, 0.96566, 0.986183]
recall_ex1 = [0.890635, 0.848706, 0.892274, 0.890635, 0.903688]
fscore_ex1 = [0.92755302, 0.88038857, 0.928441086, 0.9275553022, 0.9431358]
user_ex1 = [4, 7, 18, 24, 33]
# Create a figure and a subplot
fig, ax = plt.subplots()

# Plot the precision values on the x-axis and the recall values on the y-axis
ax.plot(user_ex1, precision_ex1, linewidth=3, linestyle='solid', label='Precision')
ax.plot(user_ex1, recall_ex1, linewidth=2, linestyle='dashed', label='Recall')
ax.plot(user_ex1, fscore_ex1, linewidth=2, linestyle='dotted', label='F1-Score')


# Add a title and labels to the axes
ax.set_title("Cluster based experiment")
ax.set_xlabel("Number of Clusters")
# ax.set_ylabel("Recall")
ax.legend()
plt.show()

# Save the figure
plt.savefig("precision_recall_cluster.png")
