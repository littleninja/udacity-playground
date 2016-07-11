# Find Eulerian Tour
#
# Write a function that takes in a graph
# represented as a list of tuples
# and return a list of nodes that
# you would follow on an Eulerian Tour
#
# For example, if the input graph was
# [(1, 2), (2, 3), (3, 1)]
# A possible Eulerian tour would be [1, 2, 3, 1]

def find_eulerian_tour(graph):

    graph_map = {}
    tour = []

    for edge in graph:
        try:
            graph_map[edge[0]].append(edge[1])
        except:
            graph_map[edge[0]] = [edge[1]]
        try:
            graph_map[edge[1]].append(edge[0])
        except:
            graph_map[edge[1]] = [edge[0]]

    # print graph_map

    for node in graph_map:
        if not tour:
            tour.append(node)
        else:
            for dest in graph_map[node]:
                # print '%s %s' % (node, dest)
                if not dest in tour:
                    tour.append(dest)
                    break

    #if tour[0] in graph_map[tour[-1]]:
    tour.append(tour[0])

    return tour


def start_end_same_node(tour):
    if tour[0] == tour[-1]:
        return True
    return False

def correct_tour_length(tour, graph):
    return len(tour) - 1 == len(graph)

def visited_all_edges_once(tour, graph):

    def edge_in_graph(s, e):
        return [i for i in graph if (i[0] == s and i[1] == e) or (i[1] == s and i[0] == e)]

    def edge_in_visited(s, e):
        return [i for i in visited if (i[0] == s and i[1] == e) or (i[1] == s and i[0] == e)]

    l = len(tour)
    visited = []

    for i in range(l-1):
        start = tour[i]
        end = tour[i + 1]
        edge = edge_in_graph(start, end)
        if not edge or edge_in_visited(start, end):
            return False
        visited += edge

    return True

def test(tour, graph):
    print graph
    print tour
    if not start_end_same_node(tour):
        print 'Tour did not start and end on the same node'
        return False
    if not correct_tour_length(tour, graph):
        print 'Tour length is incorrect: tour %s, graph %s' % (len(tour), len(graph))
        return False
    if not visited_all_edges_once(tour, graph):
        print 'Tour did not visit all edges'
        return False
    print 'Tour passes all tests'
    return True

if __name__ == '__main__':

    graph_1 = [(1, 2), (2, 3), (3, 1)]
    tour_1 = find_eulerian_tour(graph_1)

    graph_2 = [(0, 1), (1, 5), (1, 7), (4, 5),
(4, 8), (1, 6), (3, 7), (5, 9),
(2, 4), (0, 4), (2, 5), (3, 6), (8, 9)]
    tour_2 = find_eulerian_tour(graph_2)

#     tour_3 = find_eulerian_tour([(1, 13), (1, 6), (6, 11), (3, 13),
# (8, 13), (0, 6), (8, 9),(5, 9), (2, 6), (6, 10), (7, 9),
# (1, 12), (4, 12), (5, 14), (0, 1),  (2, 3), (4, 11), (6, 9),
# (7, 14),  (10, 13)])
#     tour_4 = find_eulerian_tour([(8, 16), (8, 18), (16, 17), (18, 19),
# (3, 17), (13, 17), (5, 13),(3, 4), (0, 18), (3, 14), (11, 14),
# (1, 8), (1, 9), (4, 12), (2, 19),(1, 10), (7, 9), (13, 15),
# (6, 12), (0, 1), (2, 11), (3, 18), (5, 6), (7, 15), (8, 13), (10, 17)])
    test(tour_2, graph_2)