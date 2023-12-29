class GrafoNoDirigido:
    def __init__(self):
        self.lista_adyacencia = {}

    def agregar_vertice(self, vertice):
        if vertice not in self.lista_adyacencia:
            self.lista_adyacencia[vertice] = []

    def agregar_arista(self, vertice1, vertice2):
        # Añade una arista entre vertice1 y vertice2
        if vertice1 in self.lista_adyacencia:
            self.lista_adyacencia[vertice1].append(vertice2)
        if vertice2 in self.lista_adyacencia:
            self.lista_adyacencia[vertice2].append(vertice1)

    def obtener_lista_adyacencia(self):
        return self.lista_adyacencia

    def __str__(self):
        return str(self.lista_adyacencia)

# Ejemplo de uso
grafo = GrafoNoDirigido()
grafo.agregar_vertice("A")
grafo.agregar_vertice("B")
grafo.agregar_vertice("C")
grafo.agregar_arista("A", "B")
grafo.agregar_arista("A", "C")

print(grafo.obtener_lista_adyacencia())

class GrafoNoDirigidoConPesos:
    def __init__(self):
        self.lista_adyacencia = {}

    def agregar_vertice(self, vertice):
        if vertice not in self.lista_adyacencia:
            self.lista_adyacencia[vertice] = {}

    def agregar_arista(self, vertice1, vertice2, peso):
        if vertice1 in self.lista_adyacencia and vertice2 in self.lista_adyacencia:
            self.lista_adyacencia[vertice1][vertice2] = peso
            self.lista_adyacencia[vertice2][vertice1] = peso

    def obtener_lista_adyacencia(self):
        return self.lista_adyacencia

# Ejemplo de uso
grafo = GrafoNoDirigidoConPesos()
grafo.agregar_vertice("A")
grafo.agregar_vertice("B")
grafo.agregar_vertice("C")
grafo.agregar_arista("A", "B", 5)
grafo.agregar_arista("A", "C", 3)

print(grafo.obtener_lista_adyacencia())


class GrafoDirigido:
    def __init__(self):
        self.lista_adyacencia = {}

    def agregar_vertice(self, vertice):
        if vertice not in self.lista_adyacencia:
            self.lista_adyacencia[vertice] = []

    def agregar_arista(self, vertice_origen, vertice_destino):
        if vertice_origen in self.lista_adyacencia:
            self.lista_adyacencia[vertice_origen].append(vertice_destino)

    def obtener_lista_adyacencia(self):
        return self.lista_adyacencia

# Ejemplo de uso
grafo = GrafoDirigido()
grafo.agregar_vertice("A")
grafo.agregar_vertice("B")
grafo.agregar_vertice("C")
grafo.agregar_arista("A", "B")
grafo.agregar_arista("A", "C")

print(grafo.obtener_lista_adyacencia())

