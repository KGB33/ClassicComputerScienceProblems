from basis import Graph, WeightedGraph
from CCSP.generic_search import bfs, node_to_path


def make_city_graph():
    city_graph = Graph(
        [
            "Seattle",
            "San Francisco",
            "Los Angeles",
            "Riverside",
            "Phoenix",
            "Dallas",
            "Houston",
            "Chicago",
            "Atlanta",
            "Miami",
            "Detroit",
            "Boston",
            "New York",
            "Philadelphia",
            "Washington",
        ]
    )
    # Add Edges
    city_graph.add_edge_by_vertices("Seattle", "San Francisco")
    city_graph.add_edge_by_vertices("Seattle", "Chicago")
    city_graph.add_edge_by_vertices("San Francisco", "Los Angeles")
    city_graph.add_edge_by_vertices("San Francisco", "Riverside")
    city_graph.add_edge_by_vertices("Chicago", "Riverside")
    city_graph.add_edge_by_vertices("Chicago", "Dallas")
    city_graph.add_edge_by_vertices("Chicago", "Atlanta")
    city_graph.add_edge_by_vertices("Chicago", "Detroit")
    city_graph.add_edge_by_vertices("Los Angeles", "Riverside")
    city_graph.add_edge_by_vertices("Los Angeles", "Phoenix")
    city_graph.add_edge_by_vertices("Riverside", "Phoenix")
    city_graph.add_edge_by_vertices("Dallas", "Phoenix")
    city_graph.add_edge_by_vertices("Dallas", "Houston")
    city_graph.add_edge_by_vertices("Dallas", "Atlanta")
    city_graph.add_edge_by_vertices("Atlanta", "Miami")
    city_graph.add_edge_by_vertices("Atlanta", "Washington")
    city_graph.add_edge_by_vertices("Atlanta", "Houston")
    city_graph.add_edge_by_vertices("Detroit", "Boston")
    city_graph.add_edge_by_vertices("Detroit", "New York")
    city_graph.add_edge_by_vertices("Detroit", "Washington")
    city_graph.add_edge_by_vertices("Phoenix", "Houston")
    city_graph.add_edge_by_vertices("Houston", "Miami")
    city_graph.add_edge_by_vertices("Miami", "Washington")
    city_graph.add_edge_by_vertices("Washington", "Philadelphia")
    city_graph.add_edge_by_vertices("Philadelphia", "New York")
    city_graph.add_edge_by_vertices("New York", "Boston")
    return city_graph


def make_weighted_city_graph():
    city_graph = WeightedGraph(
        [
            "Seattle",
            "San Francisco",
            "Los Angeles",
            "Riverside",
            "Phoenix",
            "Dallas",
            "Houston",
            "Chicago",
            "Atlanta",
            "Miami",
            "Detroit",
            "Boston",
            "New York",
            "Philadelphia",
            "Washington",
        ]
    )
    # Add Edges
    city_graph.add_edge_by_vertices("Seattle", "San Francisco", 678)
    city_graph.add_edge_by_vertices("Seattle", "Chicago", 1737)
    city_graph.add_edge_by_vertices("San Francisco", "Los Angeles", 348)
    city_graph.add_edge_by_vertices("San Francisco", "Riverside", 386)
    city_graph.add_edge_by_vertices("Chicago", "Riverside", 1704)
    city_graph.add_edge_by_vertices("Chicago", "Dallas", 805)
    city_graph.add_edge_by_vertices("Chicago", "Atlanta", 588)
    city_graph.add_edge_by_vertices("Chicago", "Detroit", 238)
    city_graph.add_edge_by_vertices("Los Angeles", "Riverside", 50)
    city_graph.add_edge_by_vertices("Los Angeles", "Phoenix", 357)
    city_graph.add_edge_by_vertices("Riverside", "Phoenix", 307)
    city_graph.add_edge_by_vertices("Dallas", "Phoenix", 887)
    city_graph.add_edge_by_vertices("Dallas", "Houston", 225)
    city_graph.add_edge_by_vertices("Dallas", "Atlanta", 721)
    city_graph.add_edge_by_vertices("Atlanta", "Miami", 604)
    city_graph.add_edge_by_vertices("Atlanta", "Washington", 543)
    city_graph.add_edge_by_vertices("Atlanta", "Houston", 702)
    city_graph.add_edge_by_vertices("Detroit", "Boston", 613)
    city_graph.add_edge_by_vertices("Detroit", "New York", 482)
    city_graph.add_edge_by_vertices("Detroit", "Washington", 396)
    city_graph.add_edge_by_vertices("Phoenix", "Houston", 1015)
    city_graph.add_edge_by_vertices("Houston", "Miami", 968)
    city_graph.add_edge_by_vertices("Miami", "Washington", 923)
    city_graph.add_edge_by_vertices("Washington", "Philadelphia", 123)
    city_graph.add_edge_by_vertices("Philadelphia", "New York", 81)
    city_graph.add_edge_by_vertices("New York", "Boston", 190)
    return city_graph


def city_to_city(from_city, to_city):
    bfs_result = bfs(
        from_city, lambda x: x == to_city, make_city_graph().neighbors_for_vertex
    )
    if bfs_result is None:
        print("No BFS Solution")
    else:
        path = node_to_path(bfs_result)
        print(f"Path from {from_city} to {to_city}:\n{path}")


def main():
    city_to_city("Boston", "Miami")
    city_graph = make_city_graph()
    print("\n\n", city_graph)
    city_graph = make_weighted_city_graph()
    print("\n\n", city_graph)


if __name__ == "__main__":
    main()
