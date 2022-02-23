from conn import *

class movies:
    def getDetails(self):
        self.name = input("Enter Movie Name : ")
        self.actor = input("Enter Actor Name : ")
        self.actress = input("Enter Actress Name : ")
        self.director = input("Enter Director Name : ")
        self.year_of_release = input("Enter Year of Release Name : ")

    def insert(self):
        con = connect() 
        self.getDetails() 
        con.insert(self.name,self.actor,self.actress,self.director,self.year_of_release)

    def display(self):
        con = connect()
        con.display()

    def display2(self):
        con = connect()
        actor = input("Enter Actor Name:")
        actress = input("Enter Actress Name:")
        con.display(actor,actress)   


    

obj = movies()

while(True):
    print("1 : Insert Data")
    print("2 : Display Data")
    print("3 : Display Data Based On actor name")
    print("4 : Exit")
    ch = int(input("Enter Choice : "))
    if ch == 1:
        obj.insert()
    elif ch == 2:
        obj.display()
    elif ch ==3:
        obj.display2()
    elif ch ==0:
        break
    else:
        print("Invalid CHoice....")