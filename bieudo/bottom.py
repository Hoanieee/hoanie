import matplotlib.pyplot as plt
import numpy as np

divisions = ["Div-A", "Div-B", "Div-C", "Div-D", "Div-E"]
boys_average_marks = [70, 82, 73, 65, 68]
girls_avarage_marks = [68, 67, 77, 61, 70]

index = np.arange(5)
width = 0.30

plt.bar(index, boys_average_marks, width, color='yellow', label='Boys Marks')
plt.bar(index, girls_avarage_marks, width, color="green",label='Girls Marks')

plt.title("Vertically Stacked Bar Graphs")
plt.xlabel("Divisions")
plt.ylabel("Marks")
plt.xticks(index, divisions)

plt.legend(loc='best')
plt.show()