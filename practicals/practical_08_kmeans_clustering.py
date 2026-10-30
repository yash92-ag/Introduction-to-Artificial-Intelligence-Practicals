"""
Practical 8: K-Means Clustering

Aim:
    To apply k-means clustering on a 2D store dataset, determine the optimal
    number of clusters using the Elbow Method, and visualize customer segments.

How to run:
    python practicals/practical_08_kmeans_clustering.py
"""

import pandas as pd
from sklearn.preprocessing import StandardScaler

# ---------------------------------------------------------------
# STEP 1: Store dataset (10 stores)
# ---------------------------------------------------------------
stores = pd.DataFrame({
    "StoreID": [f"St{str(i).zfill(2)}" for i in range(1, 11)],
    "DailyFootfall": [850, 900, 200, 180, 500, 520, 870, 210, 510, 890],
    "DailyRevenue_Th": [120, 130, 35, 30, 70, 75, 125, 32, 72, 128]
})

# ---------------------------------------------------------------
# STEP 2: Standardize the features (Z-score)
# ---------------------------------------------------------------
X = stores[["DailyFootfall", "DailyRevenue_Th"]]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("Store Dataset:\n", stores.head(4))
print("\nStandardized Features (First 4 rows):\n", X_scaled[:4])
print("[REASON FOR STANDARDIZATION] Footfall (hundreds) and Revenue (thousands) "
      "operate on differing numeric magnitudes.")
print("Without Z-score scaling, footfall would dominate Euclidean distance metrics.\n")

# ---------------------------------------------------------------
# STEP 3: Elbow Method (try k = 1 to 7 and record the inertia)
# Inertia = how spread out the points are inside their clusters.
# The "elbow" is where the inertia stops dropping sharply.
# ---------------------------------------------------------------
from sklearn.cluster import KMeans

inertias = []
k_range = range(1, 8)
for k in k_range:
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(X_scaled)
    inertias.append(km.inertia_)

for k, val in zip(k_range, inertias):
    note = " <-- Sharp elbow bend detected (Optimal k = 3)" if k == 3 else ""
    print(f"k = {k}: Inertia = {val:.4f}{note}")

# ---------------------------------------------------------------
# STEP 4: Fit the final model with k = 3
# ---------------------------------------------------------------
optimal_k = 3
km_final = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)
stores["Segment"] = km_final.fit_predict(X_scaled)

# STEP 5: Convert the centroids back to the original units
centroids_orig = scaler.inverse_transform(km_final.cluster_centers_)

print("\nStore Segment Assignments:")
print(stores[["StoreID", "DailyFootfall", "DailyRevenue_Th", "Segment"]])

# Name each cluster by ranking the centroid footfall (low -> high)
order = centroids_orig[:, 0].argsort()
names = {order[0]: "Low Footfall", order[1]: "Mid Performers", order[2]: "Tier-1 Flagship"}

print("\nCluster Centroids (Original Metric Units):")
for i, c in enumerate(centroids_orig):
    print(f"Cluster {i} ({names[i]}): Footfall = {c[0]:.1f}, Revenue = {c[1]:.1f}K")

# STEP 6: Mean footfall and revenue of each segment
print("\nMean Footfall & Revenue by Segment:")
print(stores.groupby("Segment")[["DailyFootfall", "DailyRevenue_Th"]].mean())
