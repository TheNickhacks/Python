# -*- coding: utf-8 -*-

# Commented out IPython magic to ensure Python compatibility.
from google.colab import drive
drive.mount("/content/drive")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin_min

# %matplotlib inline
from mpl_toolkits.mplot3d import Axes3D
plt.rcParams['figure.figsize'] = (16, 9)
plt.style.use('ggplot')
# cargamos el archivo y vemos su contenido
dataframe = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/analisis.csv")
dataframe.head()
dataframe.describe() 

# Para saber cuántos registros tenemos de cada uno hacemos:
print(dataframe.groupby('categoria').size()) 

# Veremos graficamente nuestros datos para tener una idea de la dispersión de los mismos:
dataframe.drop(['categoria'],1).hist()
plt.show() 

# En este caso seleccionamos 3 dimensiones: op, ex y ag y las cruzamos para ver si nos dan alguna pista de su agrupación y la relación con sus categorías.
sb.pairplot(dataframe.dropna(), hue='categoria',size=4,vars=["op","ex","ag"]
,kind='scatter')
# Revisando la gráfica no pareciera que haa algún tipo de agrupación o correlación entre los usuarios y sus categorías. 

# Concretamos la estructura de datos que utilizaremos para alimentar el algoritmo.
# Como se ve, sólo cargamos las columnas op, ex y ag en nuestra variable X.
X = np.array(dataframe[["op","ex","ag"]])
y = np.array(dataframe['categoria'])
X.shape

fig = plt.figure()
ax = Axes3D(fig)
colores=['blue','red','green','blue','cyan','yellow','orange','black','pink','brown','purple']
asignar=[]
for row in y:
 asignar.append(colores[row])
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=asignar,s=60)

# Vamos a hallar el valor de K haciendo una gráfica e intentando
# hallar el “punto de codo” (o líder del grupo)
# Este es nuestro resultado:
Nc = range(1, 20)
kmeans = [KMeans(n_clusters=i) for i in Nc]
kmeans
score = [kmeans[i].fit(X).score(X) for i in range(len(kmeans))]
score
plt.plot(Nc,score)
plt.xlabel('Number of Clusters')
plt.ylabel('Score')
plt.title('Elbow Curve')
plt.show() 

#Ejecutamos el algoritmo para 5 clusters y obtenemos las etiquetas y los centroids.
kmeans = KMeans(n_clusters=5).fit(X)
centroids = kmeans.cluster_centers_
print(centroids)
kmeans = KMeans(n_clusters=5).fit(X)
centroids = kmeans.cluster_centers_
print(centroids) 

# Con colores para los grupos y veremos si se diferencian:
#(las estrellas marcan el centro de cada cluster)
# Predicting the clusters
labels = kmeans.predict(X)
# Getting the cluster centers
C = kmeans.cluster_centers_
colores=['red','green','blue','cyan','yellow']
asignar=[]
for row in labels:
 asignar.append(colores[row])

fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=asignar,s=60)
ax.scatter(C[:, 0], C[:, 1], C[:, 2], marker='*', c=colores, s=1000)

# Gráfico 1
f1 = dataframe['op'].values
f2 = dataframe['ex'].values

plt.scatter(f1, f2, c=asignar, s=70)
plt.scatter(C[:, 0], C[:, 1], marker='*', c=colores, s=1000)
plt.show()
# Gráfico 2
f1 = dataframe['op'].values
f2 = dataframe['ag'].values

plt.scatter(f1, f2, c=asignar, s=70)
plt.scatter(C[:, 0], C[:, 2], marker='*', c=colores, s=1000)
plt.show()
# Gráfico 3
f1 = dataframe['ex'].values
f2 = dataframe['ag'].values

plt.scatter(f1, f2, c=asignar, s=70)
plt.scatter(C[:, 1], C[:, 2], marker='*', c=colores, s=1000)
plt.show() 

#En estas gráficas vemos que están bastante bien diferenciados los grupos.
#Podemos ver cada uno de los clusters cuantos usuarios tiene:
copy = pd.DataFrame()
copy['usuario']=dataframe['usuario'].values
copy['categoria']=dataframe['categoria'].values
copy['label'] = labels;
cantidadGrupo = pd.DataFrame()
cantidadGrupo['color']=colores
cantidadGrupo['cantidad']=copy.groupby('label').size()
cantidadGrupo 

group_referrer_index = copy['label'] ==0
group_referrals = copy[group_referrer_index]

diversidadGrupo = pd.DataFrame()
diversidadGrupo['categoria']=[0,1,2,3,4,5,6,7,8,9]
diversidadGrupo['cantidad']=group_referrals.groupby('categoria').size()
diversidadGrupo 

#vemos el representante del grupo, el usuario cercano a su centroid
closest, _ = pairwise_distances_argmin_min(kmeans.cluster_centers_, X)
closest
users=dataframe['usuario'].values
for row in closest:
 print(users[row]) 

X_new = np.array([[45.92,57.74,15.66]]) #davidguetta
new_labels = kmeans.predict(X_new)
print(new_labels)

X_new = np.array([[52.89,38.62,19.97]]) #Cristiano 
new_labels = kmeans.predict(X_new)
print(new_labels)

X_new = np.array([[31.89,53.37,24.29]]) #Falcao
new_labels = kmeans.predict(X_new)
print(new_labels)