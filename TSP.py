from itertools import permutations
# Function to calculate the total distance of a given tour
def calculate_total_distance(tour, distance_matrix):
total_distance = 0
num_cities = len(tour)
for i in range(num_cities - 1):
total_distance += distance_matrix[tour[i]][tour[i + 1]]
# Return to the starting city
total_distance += distance_matrix[tour[-1]][tour[0]]
return total_distance
# Function to solve TSP using brute force
def tsp_brute_force(distance_matrix):
num_cities = len(distance_matrix)
cities = list(range(num_cities))
# Generate all possible permutations of cities (except the starting city)
all_possible_tours = permutations(cities)
min_distance = float('inf')
best_tour = None
# Iterate over all possible tours and calculate their distances
for tour in all_possible_tours:
current_distance = calculate_total_distance(tour, distance_matrix)
#Print each tour
print(f"Tour: {tour}, Distance: {current_distance}")
if current_distance < min_distance:
min_distance = current_distance
best_tour = tour
return best_tour, min_distance
# Example distance matrix (symmetric TSP)
distance_matrix = [
[0, 10, 15, 20],
[10, 0, 35, 25],
[15, 35, 0, 30],
[20, 25, 30, 0]
]
# Solve TSP using brute force
best_tour, min_distance = tsp_brute_force(distance_matrix)

# Output the best tour and the minimum distance
print(f"Best tour: {best_tour}")
print(f"Minimum distance: {min_distance}")
