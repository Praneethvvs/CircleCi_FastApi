import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
from sklearn.cluster import KMeans

data = pd.read_excel("/home/kairos/PRANEETH_FILES/feb_11/test.xlsx")
# print(data)

x = data.loc[:,"Name":"Cluster"]

# kmeans = KMeans(7)
# kmeans.fit(x)

# identified_clusters = kmeans.fit_predict(x)
# print(identified_clusters)
# x["ResultCluster"] = identified_clusters

from sklearn import preprocessing
x_scaled = preprocessing.scale(x)

wcs =[]
# for i in range(1,22):
#     kmeans = KMeans(i)
#     kmeans.fit(x_scaled)
#     wcs_iter = kmeans.inertia_
#     wcs.append(wcs_iter)
#
#
# cluster_number = range(1,22)
# plt.plot(cluster_number,wcs)
# plt.title("Elbow Method")
# plt.xlabel("no of clusters")
# plt.ylabel("wcss values")
# plt.show()

kmeans = KMeans(10)
kmeans.fit(x_scaled)
cluster_pred = kmeans.fit_predict(x_scaled)
x["cluster_pred"] = cluster_pred

plt.scatter(x["Cluster"],x["Name"],c = x["cluster_pred"],cmap="rainbow")
plt.ylim(0,40)
plt.xlim(0,20)
plt.show()