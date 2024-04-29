import pandas as pd

# Load the dataset
df = pd.read_csv('vgsales.csv')

# Define the regions
regions = ['NA_Sales', 'EU_Sales', 'JP_Sales']

# Calculate the total sales for each region
total_sales = df[regions].sum()

# Calculate the genre proportions for each region
genre_proportions = {}
for region in regions:
    genre_proportions[region] = (df.groupby('Genre')[region].sum() / total_sales[region]).to_dict()

# Now genre_proportions contains the proportions of sales for each genre in each region
print(genre_proportions)
