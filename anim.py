import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Button

# List of CSV files to animate
csv_files = ['files/mo_archive_gen001.csv']  # Add your file names here

# Create a figure and axis for the plot
fig, ax = plt.subplots()

# Function to update the scatter plot for each frame
def update(frame):
    ax.clear()
    file_path = csv_files[frame]
    df = pd.read_csv(file_path, delimiter='|')
    x_values = df['obj1_train']
    y_values = df['obj2_train']
    ax.scatter(x_values, y_values, alpha=0.5)
    ax.set_xlabel('obj1_test')
    ax.set_ylabel('obj2_test')
    ax.set_title(f'Scatter Plot: {file_path}')

    # Set fixed limits for the x and y axes
    # ax.set_xlim(x_values.min(), x_values.max())
    # ax.set_ylim(y_values.min(), y_values.max())

# Create the animation
animation = FuncAnimation(fig, update, frames=len(csv_files), repeat=False)

# Add a "Replay" button
replay_ax = plt.axes([0.8, 0.01, 0.1, 0.05])
replay_button = Button(replay_ax, 'Replay', hovercolor='0.975')

# Function to handle button click event
def replay(event):
    animation.frame_seq = animation.new_frame_seq() 

# Attach the button click event to the replay function
replay_button.on_clicked(replay)

# Display the animation
plt.show()