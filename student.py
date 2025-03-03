from person import Person
from learner import Learner
class Student(Person,Learner):
    def __init__(self,id:int,name:str,age:int,gender:str):
        super().__init__(name,age,gender)
        Learner.__init__(self,'history')
        self.id = id

    def read(self,book):
        return f'{self.name} is reading {book}'
    def walk(self):
        value = super().walk()
        return f'{value} is returned by parent'
    
if __name__=='__main__':
    pass