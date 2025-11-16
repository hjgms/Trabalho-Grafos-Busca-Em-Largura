from collections import deque

class Grafo:
    def __init__(self):
        self.adj = {}  # lista

    def adicionar_vertice(self, v):
        if v not in self.adj:
            self.adj[v] = []

    def adicionar_aresta(self, u, v):
        """Grafo não direcionado"""
        self.adicionar_vertice(u)
        self.adicionar_vertice(v)
        self.adj[u].append(v)
        self.adj[v].append(u)

    def bfs(self, inicio):
        visitado = set()
        fila = deque([inicio])
        visitado.add(inicio)

        ordem_visita = []

        while fila:
            atual = fila.popleft()
            ordem_visita.append(atual)

            for vizinho in self.adj[atual]:
                if vizinho not in visitado:
                    visitado.add(vizinho)
                    fila.append(vizinho)

        return ordem_visita

    def menor_caminho(self, inicio, fim):
        if inicio not in self.adj or fim not in self.adj:
            return None

        fila = deque([inicio])
        visitado = set([inicio])
        pai = {inicio: None}

        while fila:
            atual = fila.popleft()

            if atual == fim:
                break

            for vizinho in self.adj[atual]:
                if vizinho not in visitado:
                    visitado.add(vizinho)
                    pai[vizinho] = atual
                    fila.append(vizinho)

        if fim not in pai:
            return None  # sem caminho

        caminho = []
        atual = fim
        while atual is not None:
            caminho.append(atual)
            atual = pai[atual]

        caminho.reverse()
        return caminho

if __name__ == "__main__":
    g = Grafo()
    g.adicionar_aresta("A", "B")
    g.adicionar_aresta("A", "C")
    g.adicionar_aresta("B", "D")
    g.adicionar_aresta("C", "D")
    g.adicionar_aresta("D", "E")

    print("BFS a partir de A:")
    print(g.bfs("A"))

    print("\nMenor caminho entre A e E:")
    print(g.menor_caminho("A", "E"))
