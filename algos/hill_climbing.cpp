#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define NUM_CITIES 4
// Distance matrix representing distances between cities
// Replace this with the actual distance matrix for your problem
int distance_matrix[NUM_CITIES][NUM_CITIES] = {
   {0, 10, 15, 20},
   {10, 0, 35, 25},
   {15, 35, 0, 30},
   {20, 25, 30, 0}
};
int total_distance(int* path, int num_cities) {
   // Calculate the total distance traveled in the given path
   int total = 0;
   for (int i = 0; i < num_cities - 1; i++) {
       total += distance_matrix[path[i]][path[i + 1]];
   }
   total += distance_matrix[path[num_cities - 1]][path[0]]; // Return to starting city
   return total;
}
void hill_climbing_tsp(int num_cities, int max_iterations) {
   int current_path[NUM_CITIES]; // Initial solution, visiting cities in order
   for (int i = 0; i < num_cities; i++) {
      current_path[i] = i;
   }
   int current_distance = total_distance(current_path, num_cities);
   for (int it = 0; it < max_iterations; it++) {
      // Generate a neighboring solution by swapping two random cities
      int neighbor_path[NUM_CITIES];
      for (int i = 0; i < num_cities; i++) {
         neighbor_path[i] = current_path[i];
      }
      int i = rand() % num_cities;
      int j = rand() % num_cities;
      int temp = neighbor_path[i];
      neighbor_path[i] = neighbor_path[j];
      neighbor_path[j] = temp;
      int neighbor_distance = total_distance(neighbor_path, num_cities);
      // If the neighbor solution is better, move to it
      if (neighbor_distance < current_distance) {
         for (int i = 0; i < num_cities; i++) {
            current_path[i] = neighbor_path[i];
         }
         current_distance = neighbor_distance;
      }
   }
   printf("Optimal path: ");
   for (int i = 0; i < num_cities; i++) {
      printf("%d ", current_path[i]);
   }
   printf("\nTotal distance: %d\n", current_distance);
}
int main() {
   srand(time(NULL));
   int max_iterations = 10000;
   hill_climbing_tsp(NUM_CITIES, max_iterations);
   return 0;
}