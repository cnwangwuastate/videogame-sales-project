import pandas as pd
from sklearn.preprocessing import RobustScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

# Read data
df = pd.read_csv('vgsales.csv')

# Prepare data for clustering
year_sales_data = df.groupby(['Year']).sum()[['NA_Sales', 'EU_Sales', 'JP_Sales']]

# Apply Robust scaling to handle outliers
scaler = RobustScaler()
scaled_data = scaler.fit_transform(year_sales_data)

# Apply K-means clustering
kmeans = KMeans(n_clusters=3)
cluster_labels = kmeans.fit_predict(scaled_data)

# Create a mapping dictionary for cluster labels based on year
cluster_mapping = dict(zip(year_sales_data.index, cluster_labels))

# Map cluster labels to the original DataFrame based on the year
df['Cluster'] = df['Year'].map(cluster_mapping)

# Create separate DataFrames for each cluster
cluster_0 = df[df['Cluster'] == 0]
cluster_1 = df[df['Cluster'] == 1]
cluster_2 = df[df['Cluster'] == 2]

# Define a function to plot genre popularity histograms
def plot_genre_histograms(cluster_df, title):
    plt.figure(figsize=(15, 8))
    sns.countplot(data=cluster_df, x='Genre', order=cluster_df['Genre'].value_counts().index, palette='viridis')
    plt.title(title)
    plt.xlabel('Genre')
    plt.ylabel('Number of Games')
    plt.xticks(rotation=45)
    plt.show()

# Plot genre popularity histograms for each cluster
plot_genre_histograms(cluster_0, 'Genre Popularity in Cluster 0 (Low and Stable Sales)')
plot_genre_histograms(cluster_1, 'Genre Popularity in Cluster 1 (Moderate and Fluctuating Sales)')
plot_genre_histograms(cluster_2, 'Genre Popularity in Cluster 2 (High and Increasing Sales)')

# Visualize clusters
plt.scatter(df['Year'], df['EU_Sales'], c=df['Cluster'], cmap='rainbow')
plt.title('Game Sales Clusters by Year (EU Sales)')
plt.xlabel('Year')
plt.ylabel('Total EU Sales')
plt.show()
