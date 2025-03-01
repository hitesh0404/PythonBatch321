
colleges=[]
from college import College,Student,Trainer
def create_college():
    name = input("Name of the college: ")
    location = input("Location of the college: ")
    colleges.append(College(name=name,location=location,students=[],trainers=[]))

def list_college():
    for index,college in enumerate(colleges):
        print(index,college)
def add_student():
    list_college()
    index = int(input("Enter the id of the college"))
    id,name,age,gender = input("enter id name age gender seperated by ,").split(',')
    colleges[index].students.append(Student(id=id,name=name,age=age,gender=gender))

def add_trainer():
    list_college()
    index = int(input("Enter the id of the college"))
    id,salary,name,age,gender = input("enter id salary name age gender seperated by ,").split(',')
    colleges[index].trainers.append(Trainer(id=id,salary=salary,name=name,age=age,gender=gender))
def list_students():
    list_college()
    i = int(input("Enter the id of the college"))
    print(type((colleges[i].students)))
    for index,student in enumerate(colleges[i].students):
        print(index,student)
def list_trainer():
    list_college()
    i = int(input("Enter the id of the college"))
    for index,student in enumerate(colleges[i].trainers):
        print(index,student)
ch=-1
def choice():
    print(f'''
    Enter 1 to create College
    Enter 2 to add Student
    Enter 3 to add Trainer
    Enter 4 to list all College
    Enter 5 to list all Student
    Enter 6 to list all Trainer
    Enter 0 to Exit
''')
    inp = int(input())
    return inp

while(ch!=0):
    ch=choice()
    if ch==1:
        create_college()
    elif ch==2:
        add_student()
    elif ch==3:
        add_trainer()
    elif ch==4:
        list_college()
    elif ch==5:
        list_students()
    elif ch==6:
        list_trainer()
    elif ch==0:
        break
    else:
        print("invalid input")
        continue