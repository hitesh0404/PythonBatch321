from person import Person
class Student(Person):
    def __init__(self,id: int, name:str, age:int, gender:str):
        super().__init__(name, age, gender)
        self.id = id  
    def __str__(self):
        return f'{self.id} {self.name} {self.age}'