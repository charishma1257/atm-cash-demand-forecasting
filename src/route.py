import pandas as pd
from math import radians, sin, cos, sqrt, atan2
from ortools.constraint_solver import pywrapcp, routing_enums_pb2

# Load ATM locations
locations = pd.read_csv("../data/atm_locations.csv")

# Example: Select first 10 ATMs for route optimization
locations = locations.head(10)

# Distance function
def distance(coord1, coord2):
    R = 6371

    lat1, lon1 = coord1
    lat2, lon2 = coord2

    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)

    a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return R * c

# Distance Matrix
coords = list(zip(locations.latitude, locations.longitude))

distance_matrix = []

for i in coords:
    row = []
    for j in coords:
        row.append(int(distance(i, j) * 1000))
    distance_matrix.append(row)

# OR-Tools
manager = pywrapcp.RoutingIndexManager(len(distance_matrix), 1, 0)
routing = pywrapcp.RoutingModel(manager)

def distance_callback(from_index, to_index):
    return distance_matrix[
        manager.IndexToNode(from_index)
    ][
        manager.IndexToNode(to_index)
    ]

transit_callback_index = routing.RegisterTransitCallback(distance_callback)

routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

search_parameters = pywrapcp.DefaultRoutingSearchParameters()

search_parameters.first_solution_strategy = (
    routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
)

solution = routing.SolveWithParameters(search_parameters)

print("\nOptimized Route\n")

index = routing.Start(0)

route = []

while not routing.IsEnd(index):
    atm = locations.iloc[manager.IndexToNode(index)]["atmId"]
    route.append(atm)
    print(atm)
    index = solution.Value(routing.NextVar(index))

# Add last ATM
atm = locations.iloc[manager.IndexToNode(index)]["atmId"]
route.append(atm)
print(atm)

# Save route
with open("../data/optimized_route.txt", "w") as f:
    for atm in route:
        f.write(str(atm) + "\n")

print("\n Route saved successfully!")