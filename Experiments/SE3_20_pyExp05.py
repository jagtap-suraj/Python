# SE-3, 20, Suraj Jagtap

#Python Experiment No. 05

"""Define a base class called Student with data members 
roll number, name, marks of three subjects and method get() to get the student details. 
Define another base class called Sports with method getsm() to read the sports mark. 
Create a new class derived from Student and Sports and define the method display() 
to find out the total and average of marks. 
Raise a user defined exception if total marks is less than 50."""

class Student:
    def __init__(self):
        self.roll_number = None
        self.name = None
        self.marks = [None, None, None]

    def get(self):
        self.roll_number = input("Enter Roll Number: ")
        self.name = input("Enter Name: ")
        for i in range(3):
            while True:
                try:
                    self.marks[i] = float(input(f"Enter Mark {i+1}: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a float value.")

class Sports:
    def __init__(self):
        self.sports_marks = None

    def getsm(self):
        self.sports_marks = float(input("Enter Sports Mark: "))

class StudentSports(Student, Sports):
    def __init__(self):
        Student.__init__(self)
        Sports.__init__(self)

    def display(self):
        total_marks = sum(self.marks) + self.sports_marks
        avg_marks = total_marks / 4
        print(f"Roll Number: {self.roll_number}")
        print(f"Name: {self.name}")
        print(f"Total Marks: {total_marks}")
        print(f"Average Marks: {avg_marks}")
        if total_marks < 50:
            raise lowerMarks("Total marks are less than 50")

class lowerMarks(Exception):
    pass 

def main():
    n = int(input("Enter the number of students: "))
    for i in range(n):
        print(f"\nEnter details of student {i+1}: ")
        s = StudentSports()
        s.get()
        s.getsm()
        try:
            s.display()
        except lowerMarks as e:
            print(e)
        except Exception as e:
            print("An error occurred:", e)

if __name__ == "__main__":
    main()
