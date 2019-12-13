from CCSP.generic_search import PriorityQueue
from basis import WeightedEdge, WeightedGraph
from Hyperloop import make_weighted_city_graph


def total_weight(wp):
    return sum([e.weight for e in wp])


def mst(wg, start=0):
    """
    Jarnik's Algorithm

        1. Pick an arbatraty vertex to start the minimum spanning tree (mst)
        2. Find the lowest edge connecting the mst to the vertiecs not yet in the mst
        3. Add the vertex at the end of that lowest edge to the mst
        4. repeate 2 & 3 untill all vertecies are in the mst

    Jarnik's Alg. might not work in graphs with directional edges, and will not work in a graph that is not connected
    """
    # (1) Make sure that starting vertex is in the graph
    if start > (wg.vertex_count - 1) or start < 0:
        return None  # Starting vertex index is outside of the graph

    result = []
    pq = PriorityQueue()
    visited = [False,] * wg.vertex_count

    # (2a) Adds all the edges to the pq, which then will pop the lowest edge
    def visit(index):
        visited[index] = True
        for edge in wg.edges_for_index(index):
            if not visited[edge.v]:
                pq.push(edge)

    visit(start)

    # (4) Repeates steps 2 & 3 untill all vertices have been visited
    while not pq.empty:
        # (2b) gets the vertex with the lowest edge from the pq
        edge = pq.pop()
        if visited[edge.v]:
            continue
        # (3) adds it to the mst
        result.append(edge)
        visit(edge.v)

    return result


def print_weighted_path(wg, wp):
    for edge in wp:
        print(f"{wg.vertex_at(edge.u)} {edge.weight} <--> {wg.vertex_at(edge.v)}")
    print(f"Total Weight: {total_weight(wp)}")


if __name__ == "__main__":
    cg = make_weighted_city_graph()
    result = mst(cg)
    if result is None:
        print("No solution Found")
    else:
        print_weighted_path(cg, result)
