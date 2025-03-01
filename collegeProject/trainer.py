from person import Person
class Trainer(Person):
    def __init__(self,id:int, salary:float, name:str, age:int, gender:str):
        super().__init__(name, age, gender)
        self.salary = salary
        self.id = id
    def __str__(self):
        return f'{self.id} {self.name} {self.age} {self.gender} {self.salary}'