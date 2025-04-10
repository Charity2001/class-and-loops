class BasicPhone:
    def ring(self):
        print("🔔 Ringgg... Ringgg...")

class SmartPhone:
    def ring(self):
        print("🎵 Custom music ringtone!")

# Test polymorphism
phones = [BasicPhone(), SmartPhone()]

for phone in phones:
    phone.ring()  
