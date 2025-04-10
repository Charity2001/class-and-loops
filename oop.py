class Phone:
    def __init__(self, brand="iPhone", model="iOS", battery=80):
        self.brand = brand  
        self.model = model  
        self.battery = battery  

    def describe(self):  
        print(f"📱 {self.brand} {self.model} | Battery: {self.battery}%")  

# Test it!
my_iphone = Phone()  
my_iphone.describe()  # Output: 📱 iPhone iOS | Battery: 80%

  def charge(self, percent):  
      self.battery += percent  
      print(f"⚡ Charged! Battery now: {self.battery}%")  

  def use(self, percent):  
      self.battery -= percent  
      print(f"🎮 Used phone! Battery left: {self.battery}%")  

# Test methods
my_iphone.charge(20)  # Output: ⚡ Charged! Battery now: 100%  
my_iphone.use(15)     # Output: 🎮 Used phone! Battery left: 85%  


battery_levels = [75, 60, 90]  # Different batteries
iphones = []  # Stores all phones

    for battery in battery_levels:
        iphone = Phone(battery=battery)  
        iphones.append(iphone) 


class ProPhone(Phone):  
    def __init__(self, battery, storage=256):  
        super().__init__(battery=battery)  # Inherits brand="iPhone", model="iOS"  
        self.storage = storage  

    def take_4k_video(self):  
        self.battery -= 10  
        print(f"🎥 Recording 4K video! Battery left: {self.battery}% | Storage: {self.storage}GB")  

# Test ProPhone
pro_iphone = ProPhone(battery=85)  
pro_iphone.describe()          # Output: 📱 iPhone iOS | Battery: 85%  
pro_iphone.take_4k_video()     # Output: 🎥 Recording 4K video! Battery left: 75% | Storage: 256GB  
# Print all iPhones
    for iphone in iphones:
        iphone.describe()  
