import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('vgsales.csv')

# List of regions
regions = ['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']

# Dictionary to store the top genres for each region
top_genres_by_region = {}

# Find the top 5 genres for each region
for region in regions:
    # Group the data by Genre and sum up sales for the current region
    genre_sales = df.groupby('Genre')[region].sum()
    
    # Get the top 5 genres
    top_genres = genre_sales.nlargest(5).index.tolist()
    
    # Store the top genres for the current region
    top_genres_by_region[region] = top_genres

# Print the top genres for each region
for region, top_genres in top_genres_by_region.items():
    print(f"Top 5 genres in {region}: {', '.join(top_genres)}")





# Plot pie charts for each region using Seaborn
for region in regions:
    # Filter the data for the top genres in the current region
    top_genre_sales = df[df['Genre'].isin(top_genres_by_region[region])].groupby('Genre')[region].sum()
    
    # Set the Seaborn style
    sns.set(style='whitegrid')

    # Plot pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(top_genre_sales, labels=top_genre_sales.index, autopct='%1.1f%%', startangle=140)
    plt.title(f'Distribution of Top 5 Genres in {region}')
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
    plt.show()


# Pie chart of video game sales by platform for each region
for region in regions:
    platform_sales = df.groupby('Platform')[region].sum().sort_values(ascending=False).head(10)
    other_platform_sales = df.groupby('Platform')[region].sum().sort_values(ascending=False).tail(-10).sum()
    platform_sales['Other'] = other_platform_sales
    platform_sales.plot(kind='pie', figsize=(8, 8), autopct='%1.1f%%', startangle=140, legend=False)
    plt.title(f'{region} Video Game Sales by Platform')
    plt.ylabel('')
    plt.show()

# Pie chart of video game sales by genre for each region
for region in regions:
    genre_sales = df.groupby('Genre')[region].sum().sort_values(ascending=False).head(10)
    other_genre_sales = df.groupby('Genre')[region].sum().sort_values(ascending=False).tail(-10).sum()
    genre_sales['Other'] = other_genre_sales
    genre_sales.plot(kind='pie', figsize=(8, 8), autopct='%1.1f%%', startangle=140, legend=False)
    plt.title(f'{region} Video Game Sales by Genre')
    plt.ylabel('')
    plt.show()

# Pie chart of video game sales by publisher for each region
for region in regions:
    publisher_sales = df.groupby('Publisher')[region].sum().sort_values(ascending=False).head(10)
    other_publisher_sales = df.groupby('Publisher')[region].sum().sort_values(ascending=False).tail(-10).sum()
    publisher_sales['Other'] = other_publisher_sales
    publisher_sales.plot(kind='pie', figsize=(8, 8), autopct='%1.1f%%', startangle=140, legend=False)
    plt.title(f'{region} Video Game Sales by Publisher')
    plt.ylabel('')
    plt.show()
