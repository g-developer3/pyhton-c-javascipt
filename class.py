class Flight():
  def __init__(self, capacity):
    self.capacity = capacity
    self.passangers = []

  def open_seats(self):
    return self.capacity - len(self.passangers)

  def add_passanger(self, name):
    if not self.open_seats():
      return False
    self.passangers.append(name)
    return True
 

flight = Flight(3)

people = ["Harry","Ron","Hermione","Ginny"]
for person in people:
  success = flight.add_passanger(person)
  if success:
    print(f"Added {person} to filght successfully.")
  else:
    print(f"No avaiable seats for {person}")