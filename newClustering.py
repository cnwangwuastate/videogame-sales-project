from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Load the dataset
df = pd.read_csv('vgsales.csv')

# List of regions
regions = ['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']

# Define the number of clusters
num_clusters = 4

# Iterate over each region
for region in regions:
    # Group by 'Year' and calculate total sales for the region
    sales_by_year_region = df.groupby('Year')[region].sum().reset_index()

    # Scale the sales data
    scaler = StandardScaler()
    scaled_sales = scaler.fit_transform(sales_by_year_region[[region]])

    # Apply K-Means clustering
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    kmeans.fit(scaled_sales)

    # Add cluster labels to the DataFrame
    sales_by_year_region['Cluster'] = kmeans.labels_

    # Analyze the clusters
    cluster_centers = scaler.inverse_transform(kmeans.cluster_centers_)
    for i, center in enumerate(cluster_centers):
        print(f"Cluster {i + 1} center for {region}: {center[0]}")

    # Genre analysis by cluster
    genre_cluster_sales = df.groupby(['Cluster', 'Genre'])[region].sum().unstack()

    # Plotting
    plt.figure(figsize=(15, 5))
    plt.suptitle(f'{region} Sales by Genre for Each Cluster')