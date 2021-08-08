def Dejkstra_method(joint):
    joint = lowest_weight_search(costs)
    while joint is not None:
        cost = costs[joint]
        neighbours = graph[joint]
        for i in neighbours.keys():
            new_cost = cost + neighbours[i]
            if costs[i] > new_cost:
                costs[i] = new_cost
                parents[i] = joint
        processed.append(joint)
        joint = lowest_weight_search(costs)


def lowest_weight_search(costs):
    lowest_cost = infinity
    lowest_cost_joint = None
    for joint in costs:
        cost = costs[joint]
        if cost < lowest_cost and joint not in processed:
            lowest_cost = cost
            lowest_cost_joint = joint
    return lowest_cost_joint


graph = dict(start={})
graph['start']['a'] = 6
graph['start']['b'] = 2
graph['a'] = {}
graph['a']['end_point'] = 1
graph['b'] = {}
graph['b']['a'] = 3
graph['b']['end_point'] = 5
graph['end_point'] = {}

processed = []
infinity = float('inf')
costs = {'a': 6, 'b': 2, 'end_point': infinity}
parents = {'a': "start", 'b': "start", 'end_point': None}

print(Dejkstra_method(graph))
