import pandas as pd
import matplotlib.pyplot as plt

# Replace 'your_file.csv' with the actual path to your CSV file
file_path = 'output_file.csv'

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(file_path, delimiter='|')

# Extract the columns for the scatter plot
x_values = df['best_fit']
y_values = [1] * len(x_values)
print(x_values)

# Create a scatter plot
plt.scatter(x_values, y_values, alpha=0.5)  # alpha controls the transparency of the points

# Set labels and title
plt.xlabel('obj1_test')
plt.ylabel('obj2_test')
plt.title('Scatter Plot: obj1_test vs obj2_test')

# Display the plot
plt.show()