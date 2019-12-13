from dataclasses import dataclass
from SpanningTree import print_weighted_path
from basis import WeightedGraph, WeightedEdge
from CCSP.generic_search import PriorityQueue
from Hyperloop import make_weighted_city_graph


@dataclass
class DijkstraNode:
    vertex: int
    distance: float

    def __lt__(self, other):
        return self.distance < other.distance

    def __eq__(self, other):
        return self.distance == other.distance


def dijkstra(wg, root):
    """
    Dijkstra's Algorithum
        - Finds the Shortest path from a starting vertex to any other vertex on a weighted graph

        1. Add the starting vertex (root) to a Priority Queue (pq)
        2. Pop the closest vertex from the pq (called current vertex)
        3. Look at all of the current vertex's (cv) neibors
            a. if the edge has not been reocored, or offeres a new shortest path then
            b. for each vertex record their distance from the start, the edge that produced this distance,
            c. and add the new vertex to the pq
        4. Repeate 2 & 3 untill the pq is empty
        5. Reuturn the shortest path from the starting vertex to every other vertex
    """
    first = wg.index_of(root)
    distances = [None,] * wg.vertex_count
    distances[first] = 0
    paths = {}
    pq = PriorityQueue()

    # (1) Adds the starting node to the pq
    pq.push(DijkstraNode(first, 0))

    # (4) loops untill pq is empty
    while not pq.empty:
        # (2) Pop the closest vertex from the pq
        u = pq.pop().vertex
        dist_u = distances[u]

        # (3) Look at all of the cv's neibors
        for we in wg.edges_for_index(u):
            dist_v = distances[we.v]

            # (3a) If this path has not been recored, or offers a new, shorter, route
            if dist_v is None or dist_v > (we.weight + dist_u):
                # (3b) Update dist to vertex
                distances[we.v] = we.weight + dist_u
                # (3b) Update path to vertex
                paths[we.v] = we
                # (3c) add to pq
                pq.push(DijkstraNode(we.v, we.weight + dist_u))

    # (5) return shortest paths
    return distances, paths


def distance_array_to_vertex_dict(wg, distances):
    return {wg.vertex_at(i): dist for i, dist in enumerate(distances)}


def path_dict_to_path(start, end, path_dict):
    if len(path_dict) == 0:
        return []

    edge_path = []
    e = path_dict[end]
    edge_path.append(e)
    while e.u != start:
        e = path_dict[e.u]
        edge_path.append(e)
    return list(reversed(edge_path))


if __name__ == "__main__":
    cg = make_weighted_city_graph()
    distances, path_dict = dijkstra(cg, "Los Angeles")
    name_distance = distance_array_to_vertex_dict(cg, distances)

    print("Distance to LA:")
    [print(f"{k}: {v}") for k, v in name_distance.items()]

    print("\n\nShortest Path from LA to Boston:")
    path = path_dict_to_path(
        cg.index_of("Los Angeles"), cg.index_of("Boston"), path_dict
    )
    print_weighted_path(cg, path)
