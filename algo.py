import heapq
from graph import ttc_graph


def find_fastest_ttc_route(start: str, end: str):
    if start not in ttc_graph:
        return float('inf'), [], f"Station not found: '{start}'"
    if end not in ttc_graph:
        return float('inf'), [], f"Station not found: '{end}'"
    if start == end:
        return 0, [start], "Already there"

    distances = {node: float('inf') for node in ttc_graph}
    previous = {node: None for node in ttc_graph}
    distances[start] = 0
    heap = [(0, start)]

    while heap:
        current_dist, current = heapq.heappop(heap)

        if current == end:
            break

        if current_dist > distances[current]:
            continue

        for neighbor, weight in ttc_graph.get(current, []):
            if neighbor not in distances:
                continue
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current
                heapq.heappush(heap, (distance, neighbor))

    if distances[end] == float('inf'):
        return float('inf'), [], "No route found"

    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous[current]
    path.reverse()

    return distances[end], path, "Success"


start = input("Enter Station: ")
end = input("Enter destination: ")

print(find_fastest_ttc_route(start, end))
