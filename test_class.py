class Build:
    year = None
    falls = None

    def __init__(self, year, falls):
        self.year = year
        self.falls = falls

    def get_data(self):
        print("Рік: ", self.year, ". Поверхів: ", self.falls, sep = '')    

class Lybrary(Build):
        books = None

        def __init__ (self, year, falls, books):
            super().__init__(year, falls)
            self.books = books
            self.get_data()
        
        def get_data(self):
            super().get_data()
            print("Кількість книг:", self.books)

class Pupils(Build):
     pupils = None

     def __init__ (self, year, falls, pupils):
          super().__init__(year, falls)
          self.pupils = pupils
          self.get_data()

     def get_data(self):
       super().get_data()
       print("Учнів:", self.pupils)

lybrary = Lybrary(1990, 2, 1000)
school = Pupils(1100, 10, 400)