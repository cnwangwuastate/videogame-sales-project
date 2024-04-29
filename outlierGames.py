import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('vgsales.csv')



## OUTLIER GAMES ##
# Calculate average sales for each genre
average_genre_sales = df.groupby('Genre')['Global_Sales'].mean()

# Determine threshold (e.g., 90th percentile)
threshold = df['Global_Sales'].quantile(0.95)

# Identify potential outlier games
outlier_games = df[df['Global_Sales'] > threshold]

# Filter outlier games by genre
outlier_games_by_genre = {}
for genre in average_genre_sales.index:
    games_for_genre = outlier_games[outlier_games['Genre'] == genre]
    
    # Check if number of games exceeds cutoff
    if len(games_for_genre) > 15:
        # Truncate DataFrame to include only top N entries
        games_for_genre = games_for_genre.nlargest(15, 'Global_Sales')
        
    outlier_games_by_genre[genre] = games_for_genre

# Plot outlier games by genre as tables
for genre, games in outlier_games_by_genre.items():
    if not games.empty:
        # Calculate total sales and percentage of total genre sales
        total_sales = games['Global_Sales'].sum()
        total_genre_sales = df[df['Genre'] == genre]['Global_Sales'].sum()
        percentage_sales = (total_sales / total_genre_sales) * 100
        
        # Append total row to DataFrame
        total_row = pd.DataFrame({'Name': ['Total'], 'Global_Sales': [total_sales]})
        games_with_total = pd.concat([games, total_row])
        
        # Append percentage of total sales row to DataFrame
        percent_row = pd.DataFrame({'Name': ['Percentage of Genre Sales'], 'Global_Sales': [percentage_sales]})
        games_with_total = pd.concat([games_with_total, percent_row])
        
        # Plot table using Seaborn heatmap
        plt.figure(figsize=(10, 6))
        sns.heatmap(games_with_total[['Name', 'Global_Sales']].set_index('Name'), annot=True, fmt='.2f', cmap='viridis', cbar=False)
        plt.title(f"Outlier games for {genre}")
        plt.xlabel('Global Sales')
        plt.ylabel('')
        plt.show()