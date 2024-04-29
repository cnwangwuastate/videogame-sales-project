import pandas as pd

# Load the dataset
df = pd.read_csv('vgsales.csv')

# Define the regions
regions = ['NA_Sales', 'EU_Sales', 'JP_Sales']

# Function to get top 10 in terms of sales for a given column and region
def get_top_10(column, region):
    top_10 = df[[column, region]].groupby(column).sum().nlargest(10, region)
    return top_10

# Get top 10 genres for each region
top_10_genres = {}
for region in regions:
    top_10_genres[region] = get_top_10('Genre', region)

# Get top 10 platforms for each region
top_10_platforms = {}
for region in regions:
    top_10_platforms[region] = get_top_10('Platform', region)

# Get top 10 publishers for each region
top_10_publishers = {}
for region in regions:
    top_10_publishers[region] = get_top_10('Publisher', region)

# Print the results
print("Top 10 Genres by Region:")
for region in regions:
    print(f"{region}:")
    print(top_10_genres[region])
    print()

print("Top 10 Platforms by Region:")
for region in regions:
    print(f"{region}:")
    print(top_10_platforms[region])
    print()

print("Top 10 Publishers by Region:")
for region in regions:
    print(f"{region}:")
    print(top_10_publishers[region])
    print()




# Load the dataset
df = pd.read_csv('vgsales.csv')

# Get the top 100 games based on global sales
top_100_games = df.nlargest(1000, 'Global_Sales')

# Count occurrences of platforms, genres, and publishers in the top 100 games
top_platforms = top_100_games['Platform'].value_counts().head(1).index[0]
top_genres = top_100_games['Genre'].value_counts().head(1).index[0]
top_publishers = top_100_games['Publisher'].value_counts().head(1).index[0]

# Print the results
print(f"The most common platform in the top 100 games is: {top_platforms}")
print(f"The most common genre in the top 100 games is: {top_genres}")
print(f"The most common publisher in the top 100 games is: {top_publishers}")

# Get the top 1000 games based on global sales
top_1000_games = df.nlargest(1000, 'Global_Sales')

# Get the top 10000 games based on global sales
top_10000_games = df.nlargest(10000, 'Global_Sales')

# Count occurrences of platforms, genres, and publishers in the top 1000 games
top_platforms_1000 = top_1000_games['Platform'].value_counts().head(1).index[0]
top_genres_1000 = top_1000_games['Genre'].value_counts().head(1).index[0]
top_publishers_1000 = top_1000_games['Publisher'].value_counts().head(1).index[0]

# Count occurrences of platforms, genres, and publishers in the top 10000 games
top_platforms_10000 = top_10000_games['Platform'].value_counts().head(1).index[0]
top_genres_10000 = top_10000_games['Genre'].value_counts().head(1).index[0]
top_publishers_10000 = top_10000_games['Publisher'].value_counts().head(1).index[0]

# Print the results
print("Results for top 1000 games:")
print(f"The most common platform is: {top_platforms_1000}")
print(f"The most common genre is: {top_genres_1000}")
print(f"The most common publisher is: {top_publishers_1000}")

print("\nResults for top 10000 games:")
print(f"The most common platform is: {top_platforms_10000}")
print(f"The most common genre is: {top_genres_10000}")
print(f"The most common publisher is: {top_publishers_10000}")
