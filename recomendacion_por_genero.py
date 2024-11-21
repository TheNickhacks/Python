import requests
import random
import math

# Configuración de la API de TMDB
api_key = '6ac0804250d9d0a9be200356343abe8e'
base_url = 'https://api.themoviedb.org/3'

# Función para obtener los géneros de una película por su ID
def obtener_generos_pelicula(movie_id):
    url = f"{base_url}/movie/{movie_id}?api_key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        detalles = response.json()
        generos = detalles.get("genres", [])
        return [genero['name'] for genero in generos]
    else:
        print(f"Error {response.status_code}: No se pudo obtener los géneros de la película con ID {movie_id}")
        return []

# IDs de películas para el ejemplo
peliculas_ids = [299536, 597, 603, 550, 578, 680, 157336, 155, 24428, 240]

# Simulación de datos de usuarios y películas con valoraciones
usuarios_peliculas = {}
peliculas_generos = {}

# Crear datos para 10 usuarios con puntuaciones y géneros
num_usuarios = 10
num_peliculas_por_usuario = 10

for usuario_id in range(1, num_usuarios + 1):
    peliculas_aleatorias = random.sample(peliculas_ids, num_peliculas_por_usuario)
    valoraciones = {}
    
    for pelicula_id in peliculas_aleatorias:
        if pelicula_id not in peliculas_generos:
            peliculas_generos[pelicula_id] = obtener_generos_pelicula(pelicula_id)
        
        # Generar una valoración aleatoria entre 1 y 5
        valoraciones[pelicula_id] = {
            'calificacion': random.randint(1, 5),
            'generos': peliculas_generos[pelicula_id]
        }
    
    usuarios_peliculas[f'usuario{usuario_id}'] = valoraciones

# print("Datos de usuarios y sus valoraciones con géneros:", usuarios_peliculas)

# --------------------------------------------
# Construcción del perfil de usuario y recomendaciones por género
# --------------------------------------------
# Función para calcular el producto punto de dos vectores
def producto_punto(x, y):
    return sum(a * b for a, b in zip(x, y))

# Función para calcular la norma de un vector
def norma(v):
    return math.sqrt(sum(a * a for a in v))

# Calcular la similitud de coseno entre dos vectores
def similitud_coseno(x, y):
    return producto_punto(x, y) / (norma(x) * norma(y)) if norma(x) * norma(y) > 0 else 0


# Crear un vocabulario de géneros únicos en todas las películas
def construir_vocabulario_generos(peliculas_generos):
    vocabulario_generos = set()
    for generos in peliculas_generos.values():
        vocabulario_generos.update(generos)
    return list(vocabulario_generos)

# Convertir géneros de cada película en un vector binario
def vectorizar_generos(generos_pelicula, vocabulario_generos):
    return [1 if genero in generos_pelicula else 0 for genero in vocabulario_generos]

# Crear un perfil de usuario en función de los géneros y sus valoraciones
def construir_perfil_usuario_generos(valoraciones, vocabulario_generos):
    perfil_usuario = [0] * len(vocabulario_generos)
    for pelicula_id, datos in valoraciones.items():
        calificacion = datos['calificacion']
        generos_pelicula = datos['generos']
        vector_generos = vectorizar_generos(generos_pelicula, vocabulario_generos)
        perfil_usuario = [p + (calificacion * g) for p, g in zip(perfil_usuario, vector_generos)]
    return perfil_usuario

# Función para recomendar películas basadas en el perfil de géneros del usuario
def recomendar_peliculas_por_genero(perfil_usuario_generos, peliculas_generos, vocabulario_generos, n_recomendaciones=5):
    similitudes = []
    for pelicula_id, generos in peliculas_generos.items():
        vector_generos = vectorizar_generos(generos, vocabulario_generos)
        similitud = similitud_coseno(perfil_usuario_generos, vector_generos)
        similitudes.append((pelicula_id, generos, similitud))
    
    # Ordenar las películas por similitud y devolver las más similares
    similitudes.sort(key=lambda x: x[2], reverse=True)
    return similitudes[:n_recomendaciones]

# Construcción del vocabulario de géneros y el perfil de usuario en función de géneros
vocabulario_generos = construir_vocabulario_generos(peliculas_generos)

# Ejemplo: construir el perfil de géneros de un usuario y recomendar películas
usuario_id = 'usuario1'  # Ejemplo con el primer usuario
perfil_usuario_generos = construir_perfil_usuario_generos(usuarios_peliculas[usuario_id], vocabulario_generos)
recomendaciones_por_genero = recomendar_peliculas_por_genero(perfil_usuario_generos, peliculas_generos, vocabulario_generos)

# Imprimir recomendaciones con géneros
print(f"Recomendaciones por género para {usuario_id}:")
for pelicula_id, generos, similitud in recomendaciones_por_genero:
    print(f"Película ID: {pelicula_id}, Géneros: {generos}, Similitud: {similitud:.2f}")
