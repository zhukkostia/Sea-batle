class Build:
    
    year = None
    city = None
    
    def __init__(self, year, city):
        self.year = year
        self.city = city

    def get_data(self):
        print(self.year, self.city) 

class School(Build):

    pupils = None

    def __init__(self, year, city, pupils):
        super().__init__(year, city)
        self.pupils = pupils
        self.get_data()
    
    def get_data(self):
        super().get_data()
        print("Учнів:", self.pupils)

school = School(1990, "Луцьк", 500)
house = Build(2006, "Львів")