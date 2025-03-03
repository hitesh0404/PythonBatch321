class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def walk(self):
        return f'{self.name} is walking'
    
    def __str__(self):
        return str(self.name) + ' of age  ' + str(self.age)
    
        