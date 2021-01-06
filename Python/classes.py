#class Point():
    #def __init__(self, x, y):
     #   self.x=x
      #  self.y=y

#p= Point(2, 8)
#print(p.x)
#print(p.y)

class Flight():
    def __init__(self, capacity):
        self.capacity= capacity
        self.passengers= []

    def addpassenger(self, name):
        if not self.openseats():
            return False       
        self.passengers.append(name)
        return True

    def openseats(self):
        return self.capacity - len(self.passengers)

flight= Flight(3)
people= ["Harry", "Ron", "Hermoine", "Ginny"]
for person in people:
    success= flight.addpassenger(person)
    if success:
        print(f"Added {person} to flight successfully.")
    else:
        print(f"No available seats for {person}")    

print(passengers)


