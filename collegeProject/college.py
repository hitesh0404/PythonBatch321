from student import Student
from trainer import Trainer
class College:
    def __init__(self, name:str, location:str, students:list,trainers:list):
        self.name = name
        self.location = location
        self.students = students
        self.trainers = trainers
    def __str__(self):
        return f'{self.name} {self.location}'