import pandas as pd
import matplotlib.pyplot as plt

#importing dataset
df = pd.read_excel("C:\\Users\\Aishwarya\\Desktop\\360DigitTMg\\Assignment6\\EastWestAirlines.xlsx\EastWestAirlines.xlsx","data")
df.head()

#Cheking ull values present and describe the data
df.isnull().sum()
df.describe()

# Normalization function 
def norm(i):
    x = (i-i.min())/(i.max()-i.min())
    return (x)

# Normalized data frame (considering the numerical part of data)
df_norm = norm(df.iloc[:, 1:])
df_norm
df_norm.describe()

#converting dataset into array
df_norm = norm(df.iloc[:, 1:].values)
df_norm

#Calculate wcss
from sklearn.cluster import KMeans
wcss = []
k = list(range(1,11))
for i in k:
    kmeans = KMeans(n_clusters = i , init = "k-means++" , random_state = 0)
    kmeans.fit(df_norm)
    wcss.append(kmeans.inertia_)
wcss

#Elbow curve
plt.plot(k , wcss)
plt.title("Elbow Curve")
plt.xlabel("No of Clusters")
plt.ylabel("wcss")


#Traing Dataset for clustering
kmeans = KMeans(n_clusters = 4)
y_kmeans = kmeans.fit_predict(df_norm)
y_kmeans

#creating a new column of cluster
cluster = pd.Series(y_kmeans)
df["Cluster"] = cluster
df

# Aggregate mean of each cluster
df.iloc[:, 1:].groupby(df.Cluster).mean()


# Visualising the clusters
plt.scatter(df_norm[y_kmeans == 0, 0], df_norm[y_kmeans == 0, 1], s = 100, c = 'red', label = 'Cluster 1')
plt.scatter(df_norm[y_kmeans == 1,0] , df_norm[y_kmeans == 1, 1] , s = 100 , c = "green" , label = "cluster 2")
plt.scatter(df_norm[y_kmeans == 2,0] , df_norm[y_kmeans == 2, 1] , s = 100 , c = "blue" , label = "cluster 3")
plt.scatter(df_norm[y_kmeans == 3,0] , df_norm[y_kmeans == 3, 1] , s = 100 , c = "orange" , label = "cluster 4")
plt.legend()
plt.show()