import pandas as pd

# Replace 'input.csv' with the path to your CSV file
csv_file = 'day.csv'

# Replace 'output.dat' with the desired name for your .dat file
dat_file = 'bikerent.dat'

# Read CSV file into a DataFrame, skipping the first row as header and the first column
df = pd.read_csv(csv_file).iloc[:, 2:]
df = df.loc[:, df.columns != 'casual']
df = df.loc[:, df.columns != 'registered']
# my_cols = set(df.columns)
 
# # removing the desired column
# my_cols.remove('season')
 
# my_cols = list(my_cols)
# df2 = df[my_cols]
# df.drop("season", axis=1)

# Write DataFrame to a .dat file (adjust format as needed)
df.to_csv(dat_file, sep=' ', header=False, index=False)