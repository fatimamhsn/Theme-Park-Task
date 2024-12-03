class Attraction:
    def __init__(self, name, capacity):
        self.__name = name
        self.__capacity = capacity
        self.__status == True

    def get_details(self):
        print(f" Attraction: {self.__name}, Capacity: {self.__capacity}")

    def open_attarction(self):
        self.__status==True

    def close_attractions(self):
        self.__status = False     


    def start(self):
        if self.__status==True:
            print("The attraction is starting")
        else:
            print('The attraction is closed')
    
class Thrillride(Attraction):
    def __init__(self, name, capacity, min_height):
        super().__init__(name, capacity)
        self.__min_height=min_height
        self.__status == True
        
    def start(self):
        if self.__status==True:
            print(f"Thrill ride {self.__name} is now starting. Hold on tight!")
        else:
            print(f"Sorry, {self.name} is closed")
        
    def is_eligible(self,height):
        if height == self.__min_height:
            return True
            
class FamilyRide(Attraction):
    def __init__(self, name, capacity, min_age):
        super().__init__(name,capacity)
        self.__min_age = min_age
        self.__status == True
    
    def start(self):
        if self.__status==True:
            print(f" Family Ride {self.__name} is now starting. Enjoy the fun!")
        else:
            print(f"Sorry, {self.name} is closed")        


    def is_eligible(self, age):
        if age == self.__min_age:
            return(True)

class Staff:
    def __init__(self, name, role):
        self.__name = name
        self.__role = role
    
    def work(self):
        print(f"Staff {self.__name} is performing their role {self.__role}")



class Manager(Staff):
    def __init__(self, name, role):
        super().__init__(name, role)
        self.__team = []

    def add_staff(self,Staff):
        self.__team.append(Staff.name)
        self.__team.append(Staff.role)

    def get_team_summary(self):
        print(self.__team)




class Visitor:
    def __init__(self, name, age, height):
        self.__name = name
        self.__age = age
        self.__height = height
        self.__ride_history = []
    
    def ride(self, Attraction):
        if isinstance(Attraction, Thrillride):
            if Thrillride.is_eligible(self.__height)==True:
                print(f"{self.__name} can ride {Attraction.__name}")
                self.__ride_history.append(Attraction.__name)
            else:
                print(f"{self.__name} cannot ride {Attraction.__name}")
        if isinstance(Attraction, FamilyRide):
            if FamilyRide.is_eligible(self.__age)==True:
                print(f"{self.__name} can ride {Attraction.__name}")
                self.__ride_history.append(Attraction.__name)
            else:
                print(f"{self.__name} cannot ride {Attraction.__name}")
    
    def view_history(self):
        print (self.__ride_history)

    

thrillride1 = Thrillride('Dragon Coaster', 20, 140)
familyride1 = FamilyRide('Flying Fish', 30, 4 )
visitor1 = Visitor('John', 22, 175 )

thrillride1.start()
familyride1.start()


visitor1.ride(Thrillride) 
visitor1.ride(FamilyRide)



     
    

    

