import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# data for the first graph
x1 = [1, 2, 3]
y1 = [4, 5, 6]

# data for the second graph
x2 = [1, 2, 3]
y2 = [4.1, 2.1, 1.1]

# plot both graphs on the same plot
plt.plot(x1, y1, linestyle='dashed')
plt.plot(x2, y2)

plt.xlabel('Precision')
plt.ylabel('Recall')
plt.title('The precision and recall of NRS')
plt.show()