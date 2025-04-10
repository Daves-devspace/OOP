#activity1

# Base class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        return f"{self.brand} {self.model}"

# Inherited class with more attributes & methods
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        super().__init__(brand, model)
        self.storage = storage
        self.battery = battery
        self.installed_apps = []

    def install_app(self, app_name):
        self.installed_apps.append(app_name)
        print(f"{app_name} installed!")

    def show_battery(self):
        print(f"Battery level: {self.battery}%")

    def __str__(self):
        return f"{self.brand} {self.model} | {self.storage}GB Storage | Battery: {self.battery}%"

# Create Smartphone objects
phone1 = Smartphone("Samsung", "Galaxy S21", 128, 85)
phone2 = Smartphone("Apple", "iPhone 13", 256, 92)

# Test
print(phone1)
phone1.install_app("Spotify")
phone1.show_battery()





#activity 2

# Base class
class Vehicle:
    def move(self):
        print("Vehicle is moving...")

# Subclasses with their own move() implementations
class Car(Vehicle):
    def move(self):
        print("🚗 Car is driving on the road.")

class Plane(Vehicle):
    def move(self):
        print("✈️ Plane is flying in the sky.")

class Boat(Vehicle):
    def move(self):
        print("🚤 Boat is sailing on water.")

# Demonstrate Polymorphism
def travel(vehicle):
    vehicle.move()

# Test
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    travel(v)

