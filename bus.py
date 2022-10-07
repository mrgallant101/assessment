from assessment.vehicle import Vehicle


class Bus(Vehicle):
    def __init__(self):
        super.__init__()
        self.maintenance = ((10/100 * self.seating_capacity) * 100)


bus = Bus()
print(bus.fare() + bus.maintenance)
