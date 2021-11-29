# Import internal library
import codecademylib3

# 1 
# Import necessary libraries
import pandas as pd
from matplotlib import pyplot as plt

# load rankings data
wood_data = pd.read_csv('Golden_Ticket_Award_Winners_Wood.csv')

# Inspect the first five rows of wood_data
print(wood_data.head())

# load rankings data
steel_data = pd.read_csv('Golden_Ticket_Award_Winners_Steel.csv')

# Inspect the first five rows of steel_data
print(steel_data.head())

# 2
# Create a function to plot rankings over time for 1 roller coaster

# Define a function with three arguments
def plot_roller_coaster(roller_coaster_name, ranking_df, park_name):
  # Assign the name of a roller coaster and the location of a roller coaster to "coaster_rankings"
  coaster_rankings = ranking_df[(ranking_df['Name'] == roller_coaster_name) & (ranking_df['Park'] == park_name)]
  # Create a figure of width 12 and height 8
  plt.figure(figsize=(12,8))
  # Create an axes object as ax
  ax = plt.subplot()
  # Plot the ranking of a given roller coaster over time as a line
  plt.plot(coaster_rankings['Year of Rank'], coaster_rankings['Rank'], marker='o', color='darkblue')
  # Set x-ticks
  ax.set_xticks(coaster_rankings['Year of Rank'].values)
  # Set y-ticks
  ax.set_yticks(coaster_rankings['Rank'].values)
  # Invert y-axis
  ax.invert_yaxis()
  # Set axis inner color
  ax.set_facecolor('whitesmoke')
  # Set title for the plot
  plt.title('{} Ranking'.format(roller_coaster_name), fontweight='bold')
  # Set x-axis label
  plt.xlabel('Year', fontweight='bold')
  # Set y-axis label
  plt.ylabel('Ranking', fontweight='bold')
  # Show plot
  plt.show()

# 3
# Create a plot of El Toro ranking over time
plot_roller_coaster('El Toro', wood_data, 'Six Flags Great Adventure')

# Clear current figure
plt.clf()

# Write a function that will plot the ranking of two given roller coasters over time as lines
def plot_two_roller_coasters(first_roller_coaster_name, first_park_name, second_roller_coaster_name, second_park_name, ranking_df):
  # Assign the first roller coaster and it's location to "first_coaster_rankings"
  first_coaster_rankings = ranking_df[(ranking_df['Name'] == first_roller_coaster_name) & (ranking_df['Park'] == first_park_name)]
  # Assign the second roller coaster and it's location to "second_coaster_rankings"
  second_coaster_rankings = ranking_df[(ranking_df['Name'] == second_roller_coaster_name) & (ranking_df['Park'] == second_park_name)]

  # Create a figure of width 12 and height 8
  plt.figure(figsize=(12, 8))
  # Create an axes object as ax1
  ax = plt.subplot()
  # Plot the rankings of the first roller coaster over time as a line
  ax.plot(first_coaster_rankings['Year of Rank'], first_coaster_rankings['Rank'], marker='o', color='cyan')
  # Plot the rankings of the second roller coaster over time as a line
  ax.plot(second_coaster_rankings['Year of Rank'], second_coaster_rankings['Rank'], marker='s', color='red')
  # Invert y-axis
  ax.invert_yaxis()
  # Set axes inner color
  ax.set_facecolor('lightyellow')
  # Set title
  plt.title('{} VS {}'.format(first_roller_coaster_name, second_roller_coaster_name), fontweight='bold')
  # Set x-axis label
  plt.xlabel('Year', fontweight='bold')
  # Set y-axis label
  plt.ylabel('Ranking', fontweight='bold')
  # Set legend
  plt.legend()
  # Show plot
  plt.show()


# Create a plot of El Toro and Boulder dash hurricanes
plot_two_roller_coasters('El Toro','Six Flags Great Adventure','Boulder Dash','Lake Compounce',wood_data)

# Clear current figure
plt.clf()
# 4
# Create a function to plot top n rankings over time
def plot_top_n(n, rankings_df):
  # Select rows with ranks less than or equal to n
  top_n_rankings = rankings_df[rankings_df['Rank'] <= n]
  # Create a figure with width 12 and height 8
  plt.figure(figsize=(12, 8))
  # Create an axes object
  ax = plt.subplot()
  # Iterate through each unique coaster in top_n_rankings
  for coaster in set(top_n_rankings['Name']):
    # Filter out the coasters with ranks less than or equal to n
    coaster_rankings = top_n_rankings[top_n_rankings['Name'] == coaster]
    # Plot the top n rankings of the coasters over time as a line
    ax.plot(coaster_rankings['Year of Rank'], coaster_rankings['Rank'], label=coaster)
   # Set y-axis ticks
  ax.set_yticks([i for i in range(1, n+1)])
  # Invert y-axis
  ax.invert_yaxis()
  # Set axes inner color
  ax.set_facecolor('snow')
  # Set title
  plt.title('Top {} Rankings'.format(n), fontweight='bold')
  # Set x label
  plt.xlabel('Year', fontweight='bold')
  # Set y label
  plt.ylabel('Ranking', fontweight='bold')
  # Set lengend
  plt.legend(loc=4)
  # Show plot
  plt.show()


# Create a plot of top n rankings over time
plot_top_n(5, wood_data)

# Clear current figure
plt.clf()

# 5
# load roller coaster data
roller_coasters = pd.read_csv('roller_coasters.csv')

# Print out roller_coasters
print(roller_coasters.head())

# 6
# Create a function to plot histogram of column values
def plot_hist(coaster_df, column_name):
  # Drop missing values
  dropna_df = coaster_df[column_name].dropna()
  # Plot histogram
  plt.hist(dropna_df)
  # Set title
  plt.title('Histogram of Roller Coaster\'s {}'.format(column_name), fontweight='bold')
  # Set x-axis label
  plt.xlabel(column_name, fontweight='bold')
  # Set y-axis label
  plt.ylabel('Count', fontweight='bold')
  # Show plot
  plt.show()

# Create histogram of roller coaster speed
plot_hist(roller_coasters, 'speed')

# Clear current figure
plt.clf()

# Create histogram of roller coaster length
plot_hist(roller_coasters, 'length')

# Clear current figure
plt.clf()

# Create histogram of roller coaster number of inversions
plot_hist(roller_coasters, 'num_inversions')

# Clear current figure
plt.clf()

# Create a function to plot histogram of height values
def plot_hist_height(coaster_df):
  # Remove outliers
  heights = coaster_df[coaster_df['height'] <= 140]
  # Drop missing values
  heights = heights['height'].dropna()
  # Plot histogram of heights
  plt.hist(heights)
  # Set title
  plt.title('Histogram of Roller Coaster\'s Height', fontweight='bold')
  # Set x-axis label
  plt.xlabel('Height', fontweight='bold')
  # Set y-axis label
  plt.ylabel('Count', fontweight='bold')
  # Show plot
  plt.show()

# Create a histogram of roller coaster height
plot_hist_height(roller_coasters)

# Clear current figure
plt.clf()

# 7
# Create a function to plot inversions by coaster at park
def plot_bar_chart_num_inversion(coaster_df, park_name):
  # Select rows that belongs to park_name
  park_coasters = coaster_df[coaster_df.park == park_name]
  # Sort park_coasters at park_name by the number of inversion in descending order
  park_coasters = park_coasters.sort_values('num_inversions', ascending=False)
  # Get the names of the roller coasters as coaster_names
  coaster_names = park_coasters.name
  # Get the number of inversions as number_inversions
  number_inversions = park_coasters.num_inversions
  # Plot bar chart
  plt.bar(range(len(number_inversions)), number_inversions)
  # Create an axes object
  ax = plt.subplot()
  # Set x-ticks
  ax.set_xticks(range(len(coaster_names)))
  # Set x-ticks labels
  ax.set_xticklabels(coaster_names, rotation=90, fontweight='bold')
  # Set title
  plt.title('Number of Inversion Per Coaster at {}'.format(park_name), fontweight='bold')
  # Set x-axis label
  plt.xlabel('Roller Coaster', fontweight='bold')
  # Set y-axis label
  plt.ylabel('Number of Inversion', fontweight='bold')
  # Show plot
  plt.show()

# Create barplot of inversions by roller coasters
plot_bar_chart_num_inversion(roller_coasters, 'Six Flags Great Adventure')

# Clear current figure
plt.clf()

# 8
# Create a function to plot a pie chart of status.operating
def plot_pie_chart(coaster_df):
  # Create a dataframe indicating the roller coasters that are operating
  operating_coasters = coaster_df[coaster_df['status'] == 'status.operating']
  # Create a dataframe indicating the roller coasters that are not operating
  closed_coasters = coaster_df[coaster_df['status'] == 'status.closed.definitely']
  # Find the length of operating_coasters and closed_coasters, save them into a list called status_counts
  status_counts = [len(operating_coasters), len(closed_coasters)]
  # Create pie chart
  plt.pie(status_counts, autopct='%0.1f%%', labels=['Operating', 'Closed'], explode=(0.1, 0), shadow=True, startangle=90)
  # Set axes to equal
  #plt.axis('equal')
  # Set title
  plt.title('Roller Coaster Status', fontweight='bold')
  # Show plot
  plt.show()

# Create pie chart of roller coasters
plot_pie_chart(roller_coasters)

# Clear current figure
plt.clf()

# 9
# Create a function to plot scatter of any two columns
def plot_scatter(coaster_df, column_x, column_y):
  # Plot scatter plot of column_y against column_x
  plt.scatter(coaster_df[column_x], coaster_df[column_y])
  # Set title
  plt.title('Scatter Plot of {} VS {}'.format(column_x, column_y), fontweight='bold')
  # Set x-axis label
  plt.xlabel(column_x, fontweight='bold')
  # Set y-axis label
  plt.ylabel(column_y, fontweight='bold')
  # Show plot
  plt.show()

# Create a scatter plot of roller coaster length by speed
plot_scatter(roller_coasters, 'speed', 'length')

# Clear current figure
plt.clf()

# Create a function to plot scatter of speed vs height
def plot_height_speed_scatter(coaster_df):
  # Remove outliers
  coaster_df = coaster_df[coaster_df.height < 140]
  # Plot a scatter plot of speed vs height
  plt.scatter(coaster_df.height, coaster_df.speed)
  # Set title
  plt.title('Scatter Plot of Speed VS Height', fontweight='bold')
  # Set x-axis label
  plt.xlabel('Height', fontweight='bold')
  # Set y-axis label
  plt.ylabel('Speed', fontweight='bold')
  # Show plot
  plt.show()

# Create a scatter plot of roller coaster height by speed
plot_height_speed_scatter(roller_coasters)