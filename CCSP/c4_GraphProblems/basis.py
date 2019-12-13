from dataclasses import dataclass


@dataclass
class Edge:
    u: int
    v: int

    def reversed(self):
        return Edge(self.v, self.u)

    def __str__(self):
        return f"{self.u} --> {self.v}"


class Graph:
    def __init__(self, vertices):
        self._vertices = vertices
        self._edges = [[] for _ in vertices]

    @property
    def vertex_count(self):
        return len(self._vertices)

    @property
    def edge_count(self):
        return sum(map(len, self._edges))

    def add_vertex(self, vertex):
        """
        Adds a vertex and returns its index
        """
        self._vertices.append(vertex)
        self._edges.append([])
        return self.vertex_count - 1

    def add_edge(self, edge):
        self._edges[edge.u].append(edge)
        self._edges[edge.v].append(edge.reversed())

    def add_edge_by_indices(self, u, v):
        edge = Edge(u, v)
        self.add_edge(edge)

    def add_edge_by_vertices(self, first, second):
        u = self._vertices.index(first)
        v = self._vertices.index(second)
        self.add_edge_by_indices(u, v)

    def vertex_at(self, index):
        return self._vertices[index]

    def index_of(self, vertex):
        return self._vertices.index(vertex)

    def neighbors_for_index(self, index):
        return list(map(self.vertex_at, [e.v for e in self._edges[index]]))

    def neighbors_for_vertex(self, vertex):
        return self.neighbors_for_index(self.index_of(vertex))

    def edges_for_index(self, index):
        return self._edges[index]

    def edges_for_vertex(self, vertex):
        return self._edges[self.index_of(vertex)]

    def __str__(self):
        desc = ""
        for i in range(self.vertex_count):
            desc += f"{self.vertex_at(i)} --> {self.neighbors_for_index(i)}\n"
        return desc


@dataclass
class WeightedEdge(Edge):
    weight: float

    def reversed(self):
        return WeightedEdge(self.v, self.u, self.weight)

    def __le__(self, other):
        return self.weight <= other.weight

    def __lt__(self, other):
        return self.weight < other.weight

    def __ge__(self, other):
        return self.weight >= other.weight

    def __gt__(self, other):
        return self.weight > other.weight

    def __str__(self):
        return f"{self.u} ({self.weight}) --> {self.v}"


class WeightedGraph(Graph):
    def add_edge_by_indices(self, u, v, weight):
        edge = WeightedEdge(u, v, weight)
        self.add_edge(edge)

    def add_edge_by_vertices(self, first, second, weight):
        u = self._vertices.index(first)
        v = self._vertices.index(second)
        self.add_edge_by_indices(u, v, weight)

    def neighbors_for_index_with_weights(self, index):
        weight_tuples = []
        for edge in self.edges_for_index(index):
            weight_tuples.append((self.vertex_at(edge.v), edge.weight))
        return weight_tuples

    def __str__(self):
        desc = ""
        for i in range(self.vertex_count):
            desc += (
                f"{self.vertex_at(i)} --> {self.neighbors_for_index_with_weights(i)}\n"
            )
        return desc


if __name__ == "__main__":
    pass
