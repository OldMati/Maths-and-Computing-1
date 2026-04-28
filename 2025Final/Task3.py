import pandas as pd

# read the file into the data frame
df = pd.read_csv('2025Final/ME1.csv')

# loop over all modules
for module in df.columns[1:]:
    # determine the maximum mark in the module
    max_mark = df[module].max()
    # print the maximum mark
    print(f'The max mark in {module} is {max_mark}')



# loop over all modules
for module in df.columns[1:]:
    # count how many students have at least 70 %
    count = df[df[module] >= 70][module].count()
    # print the result
    print(f'{count} students have achieved a mark of at least 70 % in {module}')