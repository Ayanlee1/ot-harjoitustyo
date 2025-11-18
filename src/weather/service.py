class WeatherService:
    def __init__(self):
        self.locations = []
    
    
    def add_location(self, location):
        if location not in self.locations:
            self.locations.append(location)
            return True
        return False
    

    def get_locations(self):
        return self.locations
    

    def remove_location(self, location):
        if location in self.locations:
            self.locations.remove(location)
            return True
        return False
    

    def get_weather(self, location):
        return f"{location}: 20°C, Aurinkoista"