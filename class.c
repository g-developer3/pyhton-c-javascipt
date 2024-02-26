#include <stdio.h>
#include <stdbool.h>

struct Flight {
  int capacity;
  char* passengers[100];
  int passenger_count;
};

int open_seats(struct Flight* flight) {
  return flight->capacity - flight->passenger_count;
}

bool add_passenger(struct Flight* flight, char* name) {
  if (open_seats(flight) == 0) {
    return false;
  }
  
  flight->passengers[flight->passenger_count] = name;
  flight->passenger_count++;
  
  return true;
}

int main() {
  struct Flight flight = {3, {}, 0};

  char* people[] = {"Harry", "Ron", "Hermione", "Ginny"};
  
  for (int i = 0; i < sizeof(people)/sizeof(people[0]); i++) {
    if (add_passenger(&flight, people[i])) {
      printf("Added %s to flight successfully.\n", people[i]);
    } else {
      printf("No available seats for %s\n", people[i]);
    }
  }

  return 0;
}
