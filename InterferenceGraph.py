# Interference Graph
# by Jason Zenarosa

from typing import Dict, Set

class InterferenceGraph:

    def __init__(self) -> None:
        """Creates a new Interference Graph."""
        self.vertices : Set[str] = set()
        self.edges : Dict[str, Set[str]] = {}
        
    def add_vertex(self, v):
        """Adds a new vertex to the graph."""
        if v not in self.vertices:
            self.vertices.add(v)
            self.edges[v] = set()

    def add_edge(self, v, w):
        """Adds an edge between two vertices."""
        if v not in self.vertices : raise ValueError(f"Unknown vertex {v}")
        if w not in self.vertices : raise ValueError(f"Unknown vertex {w}")
        self.edges[v].add(w)
        self.edges[w].add(v)

    def remove_vertex(self, v):
        """Removes a vertex and all its edges."""
        if v not in self.vertices : raise ValueError(f"Unknown vertex {v}")
        for w in self.edges[v] : self.edges[w].remove(v)
        del self.edges[v]
        self.vertices.remove(v)

    def remove_edge(self, v, w):
        """Removes an edge between two vertices."""
        if v not in self.vertices : raise ValueError(f"Unknown vertex {v}")
        if w not in self.vertices : raise ValueError(f"Unknown vertex {w}")
        if not self.interferes(v, w) : raise ValueError(f"Unknown edge: {v} - {w}")
        self.edges[v].remove(w)
        self.edges[w].remove(v)

    def get_vertices(self):
        """Returns a set of all vertices."""
        return self.vertices

    def neighbors(self, v):
        """Returns all edges of a vertex."""
        return self.edges[v]

    def num_vertices(self):
        """returns the number of vertices."""
        return len(self.vertices)
    
    def num_edges(self):
        """Returns the number of edges."""
        num_edges = 0
        for vertex in self.vertices:
            num_edges += len(self.edges[vertex])
        return num_edges // 2

    def interferes(self, v, w):
        """Returns true if there is an edge between v and w."""
        if v not in self.vertices : raise ValueError(f"Unknown vertex {v}")
        if w not in self.vertices : raise ValueError(f"Unknown vertex {w}")
        return w in self.neighbors(v)

    def degree(self, v):
        """Returns the number of edges a vertex has."""
        if v not in self.vertices : raise ValueError(f"Unknown vertex {v}")
        return len(self.edges[v])
