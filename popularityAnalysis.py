import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read data
df = pd.read_csv('vgsales.csv')

# Drop rows with missing values
df.dropna(inplace=True)

# Define regions
regions = ['NA_Sales', 'EU_Sales', 'JP_Sales']

# Define categories
categories = ['Platform', 'Genre', 'Publisher']

# Loop through each region
for region in regions:
    print(f"Top 10 {region} Sales by Category:")
    
    # Loop through each category
    for category in categories:
        # Calculate total sales by category
        category_sales = df.groupby(category)[region].sum().reset_index()
        
        # Sort by total sales in descending order and select top 10
        top_10_category_sales = category_sales.sort_values(by=region, ascending=False).head(10)
        
        # Print top 10 category sales
        print(f"\nTop 10 {category}:\n{top_10_category_sales}")
        
        # Visualize top 10 category sales
        plt.figure(figsize=(15, 8))
        sns.barplot(data=top_10_category_sales, x=category, y=region, palette='viridis')
        plt.title(f'Top 10 {category} Sales in {region}')
        plt.xlabel(category)
        plt.ylabel(f'Total {region} Sales')
        plt.xticks(rotation=45)
        plt.show()

