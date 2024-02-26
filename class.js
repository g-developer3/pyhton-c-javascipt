class Flight {
  constructor(capacity) {
    this.capacity = capacity;
    this.passengers = [];
  }

  openSeats() {
    return this.capacity - this.passengers.length;
  }

  addPassenger(name) {
    if (this.openSeats() === 0) {
      return false;
    }
    this.passengers.push(name);
    return true;
  }
}

const flight = new Flight(3);

const people = ["Harry", "Ron", "Hermione", "Ginny"];
for (let person of people) {
  const success = flight.addPassenger(person);
  if (success) {
    console.log(`Added ${person} to flight successfully.`);
  } else {
    console.log(`No available seats for ${person}`);
  }
}
