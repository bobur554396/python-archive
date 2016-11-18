
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn
# from sklearn.linear_model import LinearRegression
# from scipy import stats
# import pylab as pl



# seaborn.set()

from sklearn import neighbors, datasets

iris = datasets.load_iris()


X, y = iris.data, iris.target

from sklearn.decomposition import PCA
pca = PCA(n_components=2)
pca.fit(X)
X_reduced = pca.transform(X)
print ("Reduced dataset shape:", X_reduced.shape)


import pylab as pl
pl.scatter(X_reduced[:, 0], X_reduced[:,1], c=y, cmap='RdYlBu')
# pl.show()
print ("Meaning of the 2 components:")
for component in pca.components_:
    print (" + ".join("%.3f x %s" % (value, name)
                      for value, name in zip(component, iris.feature_names)))

from sklearn.cluster import KMeans
k_means = KMeans(n_clusters=3, random_state=0)
k_means.fit(X)
y_pred = k_means.predict(X)

pl.scatter(X_reduced[:, 0], X_reduced[:, 1], c=y_pred, cmap='RdYlBu')

pl.show()