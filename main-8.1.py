class vehicle:
  def setVehicleMake(self, make):
    self.VehicleMake = make

  def setVehicleModel(self, model):
    self.VehicleModel = model

  def getVehicleMake(self):
    print(f"The vehicle make: {self.VehicleMake}")
  
  def getVehicleModel(self):
    print(f"The vehicle model: {self.VehicleModel}")

class car(vehicle):
    def setCarDoor(self, car_door):
      self.CarDoor = car_door

    def getCarDoor(self):
      print(f"The number of doors: {self.CarDoor}")

class truck(vehicle):
    def setBedLength(self, bed_length):
      self.BedLength = bed_length

    def getBedLength(self):
      print(f"The bed length is: {self.BedLength}")

def main():
  print("Welcome to Ricardo's Garage! Please select your vehicle:")
  print("1. Car")
  print("2. Truck")
  select = int(input("Please input your selection: "))
  
  if select == 1:
    new_car = car()
    new_car.setVehicleMake(input("Please enter the car make: "))
    new_car.setVehicleModel(input("Please enter the car model: "))
    new_car.setCarDoor(input("Please input the number of doors: "))
    print()
    
    new_car.getVehicleMake()
    new_car.getVehicleModel()
    new_car.getCarDoor()

  elif select == 2:
    new_truck = truck()
    new_truck.setVehicleMake(input("Please enter the truck make: "))
    new_truck.setVehicleModel(input("Please enter the truck model: "))
    new_truck.setBedLength(input("Please input the bed length: "))
    print()
    
    new_truck.getVehicleMake()
    new_truck.getVehicleModel()
    new_truck.getBedLength()    

main()