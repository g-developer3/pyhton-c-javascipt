class Flight():
  
  def __init__(self,capacity):
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

people = ["Robin","Tony","Kaniya","Robin2","Jasmin"]
for person in people:
  sucess = flight.add_passanger(person)
  if sucess:
    print(f"{person} is added sucessfully.")
  else:
    print(f"not added to {person}")