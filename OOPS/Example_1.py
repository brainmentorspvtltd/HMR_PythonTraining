# Constructor Destructor
class Student():

    def __init__(self):
        self.marks = []

    def showMarks(self,name,p,c,m):
        print(name)
        self.marks.append([p,c,m])
        print("Marks :",self.marks)

    def __del__(self):
        print("Object Deleted")

obj_1 = Student()
obj_1.showMarks('Ram',50,60,55)

obj_2 = Student()
obj_2.showMarks('Shyam',50,70,88)