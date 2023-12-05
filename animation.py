import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Button

# List of CSV files to animate
# csv_files = ['front.csv', 'front2.csv', 'front3.csv', 'front4.csv', 'front5.csv', 'front6.csv', 'front7.csv', 'front8.csv', 'front9.csv', 'front10.csv']  # Add your file names here
# file_path = 'files/mo_archive_gen001.csv'

csv_directory = './ecoli'
csv_files = [file for file in os.listdir(csv_directory) if file.endswith('.csv') and file.startswith('mo')]


# Replace 'your_file.csv' with the actual path to your CSV file
file_path2 = os.path.join(csv_directory, 'symbreg.csv')

# Read the CSV file into a pandas DataFrame
df2 = pd.read_csv(file_path2, delimiter='|')

# Extract the columns for the scatter plot
x_values2 = df2['best_fit']
time_values2 = df2['time']
y_values2 = [0] * len(x_values2)


# Replace 'your_file.csv' with the actual path to your CSV file
file_path3 = os.path.join(csv_directory, 'symbregMO.csv')
df3 = pd.read_csv(file_path3, delimiter='|')
time_values3 = df3['time']

# Create a figure and axis for the plot
fig, ax = plt.subplots()

min_x, max_x, min_y, max_y = float('inf'), float('-inf'), float('inf'), float('-inf')

for file in csv_files:
    file_path = os.path.join(csv_directory, file)
    df = pd.read_csv(file_path, delimiter='|')
    x_values = df['obj1_train']
    y_values = df['obj2_train']


    # print(x_values.min(), x_values.max(), min_x, max_x)
    min_x = min(min_x, x_values.min())
    max_x = max(max_x, x_values.max())
    min_y = min(min_y, y_values.min())
    max_y = max(max_y, y_values.max())

# Function to update the scatter plot for each frame
def update(frame):
    ax.clear()
    # file_path = 'files/mo_archive_gen001.csv'
    file_path = os.path.join(csv_directory, csv_files[frame])
    df = pd.read_csv(file_path, delimiter='|')
    x_values = df['obj1_train']
    y_values = df['obj2_train']
    ax.scatter(x_values, y_values, alpha=0.5)
    # ax.scatter(x_values2[frame], y_values2[frame], alpha=0.5, color="red")
    ax.axvline(x_values2[frame], color='red', linestyle='--', label='Vertical Line at x=0.5')
    ax.set_xlabel('symbreg')
    ax.set_ylabel('phi')

    ax.set_title(f'Scatter Plot: {file_path} \n Time spend(seconds) SO: {time_values2[frame]} vs MO: {time_values3[frame]}')

    # Set fixed limits for the x and y axes
    print("final", max_x, max_y)
    ax.set_xlim(0, max_x+0.1)
    ax.set_ylim(0, max_y+1)

# Create the animation
animation = FuncAnimation(fig, update, frames=len(csv_files), repeat=False)

# Add a "Replay" button
replay_ax = plt.axes([0.8, 0.01, 0.1, 0.05])
replay_button = Button(replay_ax, 'Replay', hovercolor='0.975')

# Function to handle button click event
def replay(event):
    print("klonnkers")
    animation.frame_seq = animation.new_frame_seq() 

# Attach the button click event to the replay function
replay_button.on_clicked(replay)

# animation.save("showing.gif")
# Display the animation
plt.show()