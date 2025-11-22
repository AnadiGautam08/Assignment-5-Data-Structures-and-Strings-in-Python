"""
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message.
"""

student = {
        'Alison' : 85 ,
        'David' : 92 ,
        'Peter' : 73 ,
        'Hugo' : 64
}

name = input("Enter the student's name : ")

try :
    print(f"{name}'s marks:",student[name])
except KeyError :
    print("Student not found")