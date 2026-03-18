import heapq

def dijkstra(graph, start):
    distances = {city: float('inf') for city in graph}
    distances[start] = 0

    pq = [(0, start)]

    while pq:
        current_distance, current_city = heapq.heappop(pq)

        for neighbor, distance in graph[current_city]:
            new_distance = current_distance + distance

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(pq, (new_distance, neighbor))

    return distances


# Sample Indian cities with road distances (approx)
graph = {
    'Delhi': [('Jaipur', 280), ('Lucknow', 550)],
    'Jaipur': [('Delhi', 280), ('Ahmedabad', 660)],
    'Lucknow': [('Delhi', 550), ('Patna', 530)],
    'Ahmedabad': [('Jaipur', 660), ('Mumbai', 530)],
    'Patna': [('Lucknow', 530), ('Kolkata', 580)],
    'Mumbai': [('Ahmedabad', 530)],
    'Kolkata': [('Patna', 580)]
}

start_city = 'Delhi'
result = dijkstra(graph, start_city)

print("Shortest distances from", start_city)
for city in result:
    print(city, ":", result[city])
