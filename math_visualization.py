
import numpy as np
import matplotlib.pyplot as plt


# Task 1: Mathematical Function Visualization


x = np.linspace(-10, 10, 400)

y1 = x
y2 = x**2
y3 = np.sin(x)
y4 = np.exp(-0.1 * x) * np.cos(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y1, label='y = x', linestyle='-')
plt.plot(x, y2, label='y = x²', linestyle='--')
plt.plot(x, y3, label='y = sin(x)', linestyle='-.')
plt.plot(x, y4, label='y = e^(-0.1x) * cos(x)', linestyle=':')

plt.title('Mathematical Function Visualization')
plt.xlabel('x values')
plt.ylabel('y values')
plt.legend()
plt.grid(True)

plt.savefig('function_plot.png')
plt.close()

# Task 2:Your Own Equation

# Mixed equation combining cubic, sine, and exponential parts
y_custom = 0.02 * x**3 - 0.5 * x + np.sin(2 * x) + np.exp(-0.05 * x)

plt.figure(figsize=(10, 6))
plt.plot(x, y_custom, label='Custom Equation')

plt.title('Custom Equation Visualization')
plt.xlabel('x values')
plt.ylabel('y values')
plt.grid(True)
plt.legend()

plt.savefig('own_equation.png')
plt.close()


# Task 3: Student Score Data Visualization

students = ["S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S10"]
midterm = np.array([85, 72, 90, 66, 78, 92, 60, 74, 88, 95])
final = np.array([80, 70, 94, 68, 75, 90, 65, 72, 84, 96])

total = 0.4 * midterm + 0.6 * final

# A. Scatter Plot
plt.figure(figsize=(8, 5))
plt.scatter(midterm, final, marker='o')

plt.title('Midterm vs Final Scores')
plt.xlabel('Midterm Score')
plt.ylabel('Final Score')
plt.grid(True)

plt.savefig('score_scatter.png')
plt.close()

# B. Histogram
plt.figure(figsize=(8, 5))
plt.hist(total, bins=5)

plt.title('Distribution of Total Scores')
plt.xlabel('Total Score')
plt.ylabel('Frequency')
plt.grid(True)

plt.savefig('score_histogram.png')
plt.close()

# C. Bar Chart
plt.figure(figsize=(10, 5))
plt.bar(students, total)

plt.title('Student Total Scores')
plt.xlabel('Students')
plt.ylabel('Total Score')
plt.grid(True)

plt.savefig('score_bar_chart.png')
plt.close()


# Task 4 — Best-Fit Line

slope, intercept = np.polyfit(midterm, final, 1)

predicted_line = slope * midterm + intercept

plt.figure(figsize=(8, 5))
plt.scatter(midterm, final, label='Original Data')
plt.plot(midterm, predicted_line, label='Best-Fit Line')

plt.title('Best-Fit Line Prediction')
plt.xlabel('Midterm Score')
plt.ylabel('Final Score')
plt.legend()
plt.grid(True)

plt.savefig('score_prediction.png')
plt.close()

# Prediction examples
prediction_inputs = [50, 75, 100]

print("Prediction Examples:")
for score in prediction_inputs:
    predicted_score = slope * score + intercept
    print(f"Predicted final score for midterm {score}: {predicted_score:.2f}")
