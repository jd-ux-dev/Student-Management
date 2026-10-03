from datetime import datetime
import ast
from abc import ABC, abstractmethod

class BaseStudent(ABC):
    @abstractmethod
    def to_dict(self):
        pass

class Student(BaseStudent):
    def __init__(self, name, clas, roll, marks_val):
        self._name = name
        self._clas = clas
        self._roll = roll
        self._marks_val = marks_val

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def clas(self):
        return self._clas

    @clas.setter
    def clas(self, value):
        self._clas = value

    @property
    def roll(self):
        return self._roll

    @roll.setter
    def roll(self, value):
        self._roll = value

    @property
    def marks_val(self):
        return self._marks_val

    @marks_val.setter
    def marks_val(self, value):
        self._marks_val = value

    def to_dict(self):
        return {"Name": self._name, "Class": self._clas, "Roll no.": self._roll, "Marks": self._marks_val}


class StudentManagementSystem:
    def __init__(self):
        f = open("Student_Management_System.txt", "a+")
        f.close()

    def showrecords(self):
        f = open("Student_Management_System.txt")
        a = f.read()
        print(a)
        f.close()

    def marks(self):
        a = int(input("Enter the number of subjects: "))
        if a == 0:
            a = 1
        s = 0
        n = 0
        while n < a:
            try:
                print("Subject", n + 1)
                b = float(input("Enter marks of the subject: "))
                if b > 100 or b < 0: 
                    raise ValueError
                s += b
                n += 1
            except ValueError:
                print("ONLY FLOAT TYPE AND NUMBERS BETWEEN 0 AND 100!")
        return s / a

    def addrecords(self):
        f = open("Student_Management_System.txt", "a+")
        while True:
            try:
                name = input("Enter Student's Name:")
                clas = int(input("Enter Class:"))
                if clas > 12:
                    raise ValueError
                roll = int(input("Enter roll no.:"))
                
                stu = Student(name, clas, roll, self.marks())
                d = str(stu.to_dict()) + "\n"
                
                f.write(d)
                f.flush()
                break
            except ValueError:
                print("STRING FOR NAME AND INTEGER FOR ROLL  NUMBER AND CLASS (UPTO 12) ONLY!")
        f.close()

    def fetchrecord(self):
        f = open("Student_Management_System.txt")
        a = f.readlines()
        x = 0
        while True:
            print('''How would you like to search records?
    * Search by name: enter 1
    *Search by roll: enter 2
     *Search by Class: enter 3''')
            try:
                b = int(input("Enter your Choice:"))
                if str(b) not in "123":
                    raise ValueError
                break
            except ValueError:
                print("Enter 1 ,2, or 3")
        
        while True:
            try:
                c = input("Enter to search:")
                if b == 1:
                    matches = [i for i in a if "'Name': '" + str(c) + "'" in i]
                    for i in matches:
                        print(i)
                        print("Line:", a.index(i) + 1)
                        x += 1
                elif b == 2:
                    c = int(c)
                    matches = [i for i in a if "'Roll no.': " + str(c) in i]
                    for i in matches:
                        print(i)
                        print("Line:", a.index(i) + 1)
                        x += 1
                elif b == 3:
                    c = int(c)
                    matches = [i for i in a if "'Class': " + str(c) in i]
                    for i in matches:
                        print(i)
                        print("Line:", a.index(i) + 1)
                        x += 1
                break
            except ValueError:
                print("Try again") 
        if x == 0:
            print("Not found")
        f.close()

    def deone(self, n):
        f = open("Student_Management_System.txt", "r")
        l = f.readlines()
        f.close()
        f = open("Student_Management_System.txt", "w")
        print("Removing ", l[n])
        del l[n]
        for i in l:
            f.write(i)
        f.flush()
        f.close()

    def delone(self):
        while True:
            try:
                f = open("Student_Management_System.txt", "r")
                l = f.readlines()
                f.close()
                n = int(input("Enter the Line number:"))
                print(l[n - 1], "to be deleted")
                if n > len(l) or n <= 0:
                    print("Only enter from 1 to", len(l))
                    raise ValueError
                a = input("ARE YOU SURE YOU WANT TO DELETE  DATA?(y/n)")
                if a == "n":
                    print("NOT DELETED")
                    break
                elif a == "y":
                    print("DATA DELETED")
                    self.deone(n - 1)
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Try again!")

    def deleteall(self):
        while True:
            try:
                a = input("ARE YOU SURE YOU WANT TO DELETE ALL DATAS?(y/n)")
                if a == "n":
                    print("NOT DELETED")
                elif a == "y":
                    print("ALL DATAS DELETED")
                    f = open("Student_Management_System.txt", "w")
                    f.close()
                else:
                    raise ValueError
                break
            except ValueError:
                print("Try again")  

    def update(self):
        f = open("Student_Management_System.txt", "a+")
        f.seek(0)
        l = f.readlines()
        while True:
            try:
                n = int(input("Which line do you want to update?"))
                if len(l) == 0:
                     print("No data to update")
                     return
                if n > len(l) or n <= 0:
                    print("Only enter from 1 to", len(l))
                    raise ValueError
                else:
                    print("The line to be updated:", l[n - 1])
                    name = input("Update Student's Name:")
                    clas = int(input("Update Class:"))
                    if clas > 12:
                        raise ValueError
                    roll = int(input("Update roll no.:"))
                    
                    stu = Student(name, clas, roll, self.marks())
                    d = str(stu.to_dict()) + "\n"
                    
                    l[n - 1] = str(d)
                    f = open("Student_Management_System.txt", "w")
                    for i in l:
                        f.write(i)
                    break
            except ValueError:
                print("Try again")


if __name__ == "__main__":
    sms = StudentManagementSystem()
    while True:
        print('''\nStudent Management System
* 1 to see records
* 2 to add records
* 3 to search records
* 4 to delete one data
* 5 to delete all data
* 6 to update data
* 7 to exit program''')
        
        try:
            choice = int(input("Enter your option (1-7): "))
            if choice == 1:
                sms.showrecords()
            elif choice == 2:
                sms.addrecords()
            elif choice == 3:
                sms.fetchrecord()
            elif choice == 4:
                sms.delone()
            elif choice == 5:
                sms.deleteall()
            elif choice == 6:
                sms.update()
            elif choice == 7:
                print("Thank you for using the system. Goodbye!")
                break
            else:
                print("Invalid option. Please choose between 1 and 7.")
        except ValueError:
            print("Please enter a valid number selection.")
        finally:
            print('''*****************************************************************************************************************************
            
            
            ''')
