#Importe de Bibliotecas respectivas
import PyPDF2
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
import re
import openpyxl
import pickle
import numpy as np
import matplotlib.pyplot as plt

#Carga de los Metadatos denomidados como Edad y Genero

Mdatos = open("datos.txt")
Lineas = Mdatos.readlines()
Metadatos = []
for linea in Lineas:
    Metadatos.append([int(x) for x in linea.split()])
Mdatos.close()

#Primero se cargaran las preguntas sobre la democracia

#MODELADO DE DOCUMENTOS
#PREGUNTAS DEMOCRACIA
Preg = open("preg_democracia.txt","r",encoding="utf-8")
Doc = Preg.readlines()
Preg.close()
len(Doc) #tamaño de los documentos almacenados
#print(Doc)

#Limpieza de documento y vectorizacion Documento Democracia
Stopw = stopwords.words('spanish')
#ngram_range para palabras individuales
vectorizarDemo = TfidfVectorizer(stop_words= Stopw, ngram_range=(1,1))
VectDocDemo = vectorizarDemo.fit_transform(Doc)
#print(VectDocDemo) 

#Creacion de la base de datos Democracia
densidadDemo = VectDocDemo.todense()
ListaDensidadDemo = densidadDemo.tolist()
Nombre_ColumnasDemo = vectorizarDemo.get_feature_names_out()
BaseDatosDemo = pd.DataFrame(ListaDensidadDemo, columns=Nombre_ColumnasDemo)
#print(Nombre_ColumnasDemo)
#print(BaseDatosDemo)

#PREGUNTAS RESPETO
PregR = open("preg_respeto.txt","r",encoding="utf-8")
DocR = PregR.readlines()
PregR.close()
len(DocR)
#print(DocR)

#Limpieza y Vectorizacion Documento Respeto
vectorizarResp = TfidfVectorizer(stop_words=Stopw, ngram_range=(1,1))
VectDocResp = vectorizarResp.fit_transform(DocR)
#print(VectDocResp)

#Creacion de la base de datos Respeto
densidadResp = VectDocResp.todense()
ListaDensidadResp = densidadResp.tolist()
Nombre_ColumnasResp = vectorizarResp.get_feature_names_out()
BaseDatosResp = pd.DataFrame(ListaDensidadResp, columns=Nombre_ColumnasResp)
#print(Nombre_ColumnasResp)
#print(BaseDatosResp)

#REDUCCION DIMENSIONAL POR RESPUESTAS
from sklearn.decomposition import PCA  # to apply PCA
import seaborn as sns  # to plot the heat maps
from sklearn.decomposition import TruncatedSVD
from scipy.sparse import csr_matrix
from sklearn.preprocessing import StandardScaler
Escalar = StandardScaler(with_mean=False)

#PREGUNTAS DEMOCRACIA
#Escalador de la vectorizacion de documento de democracia
print("\n Reduccion Dimensional para Democracia \n")
Escalar_dataDemo = Escalar.fit_transform(VectDocDemo) 

VSTDemo = TruncatedSVD(n_components= 2) #Reduccion a dos componentes
DSVDDemo = VSTDemo.fit_transform(Escalar_dataDemo)
print(VSTDemo.explained_variance_ratio_)
print(VSTDemo.explained_variance_)
print(VSTDemo.explained_variance_ratio_.sum())
print(VSTDemo.singular_values_)
BaseRDDemo = pd.DataFrame(DSVDDemo, columns=['D1','D2'])
print(BaseRDDemo)

#PREGUNTAS RESPETO
print("\n Reduccion Dimensional para Respeto \n")
Escalar_dataResp = Escalar.fit_transform(VectDocResp) 

VSTResp = TruncatedSVD(n_components= 2) #Reduccion a dos componentes
DSVDResp = VSTResp.fit_transform(Escalar_dataResp)
print(VSTResp.explained_variance_ratio_)
print(VSTResp.explained_variance_)
print(VSTResp.explained_variance_ratio_.sum())
print(VSTResp.singular_values_)
BaseRDResp = pd.DataFrame(DSVDResp, columns=['D1','D2'])
print(BaseRDResp)

#REDUCCION DIMENSIONAL POR PALABRAS
EscalarPalabras = StandardScaler(with_mean=False)
#PALABRAS DEMOCRACIA
print("\n Reduccion Dimensional Palabras para Democracia \n")
Escalar_dataPalDemo = EscalarPalabras.fit_transform(VectDocDemo)

VSTPalDemo = TruncatedSVD(n_components= 2) #Reduccion a dos componentes
DSVDPalDemo = VSTPalDemo.fit_transform(Escalar_dataPalDemo.transpose())
print(VSTPalDemo.explained_variance_ratio_)
print(VSTPalDemo.explained_variance_)
print(VSTPalDemo.explained_variance_ratio_.sum())
print(VSTPalDemo.singular_values_)
BaseRDPalDemo = pd.DataFrame(DSVDPalDemo, columns=['D1','D2'])
print(BaseRDPalDemo)

#PALABRAS RESPETO
print("\n Reduccion Dimensional Palabras para Respeto \n")

Escalar_dataPalResp = EscalarPalabras.fit_transform(VectDocResp)

VSTPalResp = TruncatedSVD(n_components= 2) #Reduccion a dos componentes
DSVDPalResp = VSTPalResp.fit_transform(Escalar_dataPalResp.transpose())
print(VSTPalResp.explained_variance_ratio_)
print(VSTPalResp.explained_variance_)
print(VSTPalResp.explained_variance_ratio_.sum())
print(VSTPalResp.singular_values_)
BaseRDPalResp = pd.DataFrame(DSVDPalResp, columns=['D1','D2'])
print(BaseRDPalResp)

#ELIMINACION DE OUTLIERS MAX Y MIN

#RESPUESTAS DEMOCRACIA

AuxDemo = list(BaseRDDemo["D1"])
AuxDDemo = list(BaseRDDemo["D2"])

ProvDemo = AuxDemo.index(max(BaseRDDemo["D1"]))
del AuxDemo[ProvDemo]
del AuxDDemo[ProvDemo]
ProvdDemo = AuxDDemo.index(max(BaseRDDemo["D2"]))
del AuxDemo[ProvdDemo]
del AuxDDemo[ProvdDemo]

DatosDemo = pd.DataFrame([AuxDemo, AuxDDemo]).transpose()
print("\nIndices de Extremos Eliminados en D1 y D2 Respuestas Democracia")
print(ProvDemo, ProvdDemo)

#RESPUESTAS RESPETO

AuxResp = list(BaseRDResp["D1"])
AuxDResp = list(BaseRDResp["D2"])

ProvResp = AuxResp.index(max(BaseRDResp["D1"]))
del AuxResp[ProvResp]
del AuxDResp[ProvDemo]
ProvdResp = AuxDResp.index(max(BaseRDResp["D2"]))
del AuxResp[ProvdResp]
del AuxDResp[ProvdResp]
DatosResp = pd.DataFrame([AuxResp, AuxDResp]).transpose()
print("\nIndices de Extremos Eliminados en D1 y D2 Respuestas Respeto")
print(ProvResp, ProvdResp)

#PALABRAS DEMOCRACIA
print("\nPalabras Democracia Eliminacion de Outliers Mayores a 1")
xBaseDemo = list(BaseRDPalDemo["D1"])
yBaseDemo = list(BaseRDPalDemo["D2"])

xAD=[]
yAD=[]
col_namesor = Nombre_ColumnasDemo
Nombre_ColumnasDemo = []
des = max(np.std(xBaseDemo), np.std(yBaseDemo))
des = 0.5
cc=[]
for i in range(len(xBaseDemo)):
    if xBaseDemo[i]<des and yBaseDemo[i]<des:
        xAD.append(xBaseDemo[i])
        yAD.append(yBaseDemo[i])
        Nombre_ColumnasDemo.append(col_namesor[i])
    else:
        cc.append([xBaseDemo[i], yBaseDemo[i]])

DataPDemo = pd.DataFrame([xAD, yAD]).transpose()
print(DataPDemo)

#PALABRAS RESPETO
print("\nPalabras Respeto Eliminacion de Outliers Mayores a 1")
xBaseResp = list(BaseRDPalResp["D1"])
yBaseResp = list(BaseRDPalResp["D2"])

xAR=[]
yAR=[]
col_namesorR = Nombre_ColumnasResp
Nombre_ColumnasResp = []
des = max(np.std(xBaseResp), np.std(yBaseResp))
des = 0.5
cc=[]
for i in range(len(xBaseResp)):
    if xBaseResp[i]<des and yBaseResp[i]<des:
        xAR.append(xBaseResp[i])
        yAR.append(yBaseResp[i])
        Nombre_ColumnasResp.append(col_namesorR[i])
    else:
        cc.append([xBaseResp[i], yBaseResp[i]])

DataPResp = pd.DataFrame([xAR, yAR]).transpose()
print(DataPResp)

#CLUSTERING 
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram

#RESPUESTAS DEMOCRACIA

modelo_hclust_completeDemo = AgglomerativeClustering(
                            metric =  'euclidean',
                            linkage  = 'complete',
                            distance_threshold = 0,
                            n_clusters         = None
                        )
modelo_hclust_completeDemo.fit(X=DatosDemo)

modelo_hclust_averageDemo = AgglomerativeClustering(
                            metric = 'euclidean',
                            linkage  = 'average',
                            distance_threshold = 0,
                            n_clusters         = None
                        )
modelo_hclust_averageDemo.fit(X=DatosDemo)

modelo_hclust_wardDemo = AgglomerativeClustering(
                            metric = 'euclidean',
                            linkage  = 'ward',
                            distance_threshold = 0,
                            n_clusters         = None
                     )
modelo_hclust_wardDemo.fit(X=DatosDemo)

#RESPUESTAS RESPETO
modelo_hclust_completeResp = AgglomerativeClustering(
                            metric = 'euclidean',
                            linkage  = 'complete',
                            distance_threshold = 0,
                            n_clusters         = None
                        )
modelo_hclust_completeResp.fit(X=DatosResp)

modelo_hclust_averageResp = AgglomerativeClustering(
                            metric = 'euclidean',
                            linkage  = 'average',
                            distance_threshold = 0,
                            n_clusters         = None
                        )
modelo_hclust_averageResp.fit(X=DatosResp)

modelo_hclust_wardResp = AgglomerativeClustering(
                            metric = 'euclidean',
                            linkage  = 'ward',
                            distance_threshold = 0,
                            n_clusters         = None
                     )
modelo_hclust_wardResp.fit(X=DatosResp)

#Dendogramas Basado en codigo visto en clases

def plot_dendrogram(model, **kwargs):
    counts = np.zeros(model.children_.shape[0])
    n_samples = len(model.labels_)
    for i, merge in enumerate(model.children_):
        current_count = 0
        for child_idx in merge:
            if child_idx < n_samples:
                current_count += 1  # leaf node
            else:
                current_count += counts[child_idx - n_samples]
        counts[i] = current_count

    linkage_matrix = np.column_stack([model.children_, model.distances_,
                                      counts]).astype(float)

    # Plot
    dendrogram(linkage_matrix, **kwargs)

#Graficas Dendogramas Respuestas Democracia
fig, axs = plt.subplots(3, 1, figsize=(8, 8))
plot_dendrogram(modelo_hclust_averageDemo, color_threshold=0, ax=axs[0])
axs[0].set_title("Distancia euclídea, Enlace Average, Respuestas Democracia")

plot_dendrogram(modelo_hclust_completeDemo, color_threshold=0, ax=axs[1])
axs[1].set_title("Distancia euclídea, Enlace Complete, Respuestas Democracia")

plot_dendrogram(modelo_hclust_wardDemo, color_threshold=0, ax=axs[2])
axs[2].set_title("Distancia euclídea, Enlace Ward, Respuestas Democracia")

plt.tight_layout()

#Graficas Dendogramas Respuestas Respeto
fig, axs = plt.subplots(3, 1, figsize=(8, 8))
plot_dendrogram(modelo_hclust_averageResp, color_threshold=0, ax=axs[0])
axs[0].set_title("Distancia euclídea, Enlace Average, Respuestas Respeto")

plot_dendrogram(modelo_hclust_completeResp, color_threshold=0, ax=axs[1])
axs[1].set_title("Distancia euclídea, Enlace Complete, Respuestas Respeto")

plot_dendrogram(modelo_hclust_wardResp, color_threshold=0, ax=axs[2])
axs[2].set_title("Distancia euclídea, Enlace Ward, Respuestas Respeto")

plt.tight_layout()
#plt.show()

#Densidad Clustero Respuestas Democracia
from sklearn.cluster import DBSCAN

modelo_dbscan = DBSCAN(
                    eps          = 0.2,
                    min_samples  = 5,
                    metric       = 'euclidean',
                )

modelo_dbscan.fit(X=DatosDemo)

labdb = modelo_dbscan.labels_
#print(labdb)

#Densidad Clustero Respuestas Respeto
from sklearn.cluster import DBSCAN

modelo_dbscan = DBSCAN(
                    eps          = 0.2,
                    min_samples  = 5,
                    metric       = 'euclidean',
                )

modelo_dbscan.fit(X=DatosResp)

labdbRes = modelo_dbscan.labels_
#print(labdbRes)

#Grafica Cluster Densidad Respuestas Democracia
fig, ax = plt.subplots(1, 1, figsize=(9, 9))

ax.scatter(DatosDemo[0], DatosDemo[1], c=labdb, alpha=0.4)

plt.rcParams["figure.figsize"] = (20, 20)

for i in range(len(DatosDemo)):
  plt.text(DatosDemo[0][i]+0.0, DatosDemo[1][i]+0.0, str(i), fontsize=6)

ax.legend()
ax.set_title('Clusterings generados por DBSCAN Respuestas Democracia');


#Grafica Cluster Densidad Respuestas Respeto
fig, ax = plt.subplots(1, 1, figsize=(9, 9))

ax.scatter(DatosResp[0], DatosResp[1], c=labdbRes, alpha=0.4)

plt.rcParams["figure.figsize"] = (20, 20)

for i in range(len(DatosResp)):
  plt.text(DatosResp[0][i]+0.0, DatosResp[1][i]+0.0, str(i), fontsize=6)

ax.legend()
ax.set_title('Clusterings generados por DBSCAN Respuestas Respeto');

#Cluster Kmeans Respuestas Democracia
from sklearn.cluster import KMeans

modelo_kmeans = KMeans(n_clusters=3, random_state=0).fit(DatosDemo)
labkmean = modelo_kmeans.labels_
#print(labkmean)

#Cluster Kmeans Respuestas Respeto
modelo_kmeansResp = KMeans(n_clusters=3, random_state=0).fit(DatosResp)
labkmeanResp = modelo_kmeansResp.labels_
#print(labkmeanResp)

#Grafica Cluster Kmeans Respuestas Democracia

fig, ax = plt.subplots(1, 1, figsize=(9, 9))

ax.scatter(DatosDemo[0], DatosDemo[1], c=labkmean, alpha=0.4)

plt.rcParams["figure.figsize"] = (20, 20)

for i in range(len(DatosDemo)):
  plt.text(DatosDemo[0][i]+0.0, DatosDemo[1][i]+0.0, str(i), fontsize=6)
ax.legend()
ax.set_title('Clusterings generados por KMeans Respuestas Democracia');


#Grafica Cluster Kmeans Respuestas Respeto

fig, ax = plt.subplots(1, 1, figsize=(9, 9))

ax.scatter(DatosResp[0], DatosResp[1], c=labkmeanResp, alpha=0.4)

plt.rcParams["figure.figsize"] = (20, 20)

for i in range(len(DatosResp)):
  plt.text(DatosResp[0][i]+0.0, DatosResp[1][i]+0.0, str(i), fontsize=6)
ax.legend()
ax.set_title('Clusterings generados por KMeans Respuestas Respeto');

#Kmeans Palabras Democracia
modelo_kmeans = KMeans(n_clusters=3, random_state=0).fit(DataPDemo)

labkmeanpal = modelo_kmeans.labels_
#print(labkmeanpal)

#Kmeans Palabras Respeto
modelo_kmeansResps = KMeans(n_clusters=3, random_state=0).fit(DataPResp)

labkmeanpalresp = modelo_kmeansResps.labels_
#print(labkmeanpalresp)

#Grafica Cluster Kmeans Palabras Democracia
fig, ax = plt.subplots(1, 1, figsize=(9, 9))
ax.scatter(DataPDemo[0], DataPDemo[1], c=labkmeanpal, alpha=0.4)

plt.rcParams["figure.figsize"] = (20, 20)

for i in range(len(DataPDemo)):
  plt.text(DataPDemo[0][i]+0.0, DataPDemo[1][i]+0.0, Nombre_ColumnasDemo[i], fontsize=6)

ax.legend()
ax.set_title('Clusterings generados por K-Means (Palabras Democracia)');

#Grafica Cluster Kmeans Palabras Respeto
fig, ax = plt.subplots(1, 1, figsize=(9, 9))
ax.scatter(DataPResp[0], DataPResp[1], c=labkmeanpalresp, alpha=0.4)

plt.rcParams["figure.figsize"] = (20, 20)

for i in range(len(DataPResp)):
  plt.text(DataPResp[0][i]+0.0, DataPResp[1][i]+0.0, Nombre_ColumnasResp[i], fontsize=6)

ax.legend()
ax.set_title('Clusterings generados por K-Means (Palabras Respeto)');


# Análisis de Correlación Pregunta 1

correlation = DatosResp.corrwith(DatosDemo)
# Visualización de Correlación
plt.figure(figsize=(8, 6))
sns.barplot(x=correlation.index, y=correlation.values)
plt.title('Correlación entre Obtención de Respeto y Manifestación de Democracia')
plt.xlabel('Variables relacionadas con Obtención de Respeto')
plt.ylabel('Correlación con Manifestación de Democracia')


# Estadísticas descriptivas para Respuestas Respeto
descriptivas_respeto = DatosResp.describe()
print("\nEstadisticos Basicos de Reduccion de Dimension de Respuestas Respeto")
print(descriptivas_respeto)

correlation = DatosResp.corr()
print("\n")
print(correlation)
print("\n")

#Pregunta 3
import seaborn as sns

# Separar las listas dentro de la tupla usando comprensión de listas
columna1 = [elemento[0] for elemento in Metadatos]
columna2 = [elemento[1] for elemento in Metadatos]

# Histograma de Respuestas Democracia (Variable D1)
sns.histplot(columna1, bins=20, kde=True)
plt.title('Distribución de Respuestas Democracia (Variable D1)')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.show()

# Gráfico de barras para géneros
sns.histplot(columna2, bins=20, color='blue')
plt.title('Distribución de Géneros')
plt.xlabel('Género')
plt.ylabel('Cantidad')
plt.show()
