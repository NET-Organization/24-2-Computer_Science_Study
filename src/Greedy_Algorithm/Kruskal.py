class Kruskal () :

    def __init__ (self, graph : dict) :
        self.parent = dict()
        self.rank = dict()
        self.graph = graph
        self.mst = self.kruskal()
        
    def make_singleton_set (self, vertex : str) :
        self.parent[vertex] = vertex
        self.rank[vertex] = 1

    def find (self, vertex : str) :
        if (self.parent[vertex] != vertex) :
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, x : str, y : str) :
        if (x != y) :
            if (self.rank[x] > self.rank[y]) :
                self.parent[y] = x
                self.rank[x] += self.rank[y]
            else :
                self.parent[x] = y
                self.rank[y] += self.rank[x]
        
    def kruskal (self) :
        edges = sorted(self.graph["edges"])
        F = set()

        for vertex in self.graph["vertices"] :
            self.make_singleton_set(vertex)

        for edge in edges :
            w, i, j = edge
            x = self.find(i)
            y = self.find(j)

            if (x != y) :
                self.union(x, y)
                F.add(edge)
                
        return F

    def return_mst (self) :
        return self.mst


if (__name__ == "__main__") :
    graph = { 'vertices': ['A', 'B', 'C', 'D', 'E'], 
          'edges': set([(1, 'A', 'B'), (3, 'A', 'C'), (3, 'B', 'C'), (6, 'B', 'D'), (4, 'C', 'D'), (2, 'C', 'E'), (5, 'D', 'E')])}

    mst = Kruskal(graph)
    print(mst.return_mst())
