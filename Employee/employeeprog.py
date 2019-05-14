# Name: employeeprog.py
#
# Description:
# This program uses the Employee class to manage an Employee.
#
# Author: Chenzhikang
# 
# Date: Match 2019
#

from employee_modulepy2 import Employee

def main():
    name = input("\n\tEnter the employee's name: ")
    employee = Employee(name)
    emp2 = Employee("Biff")

    selection = 'a';
    while selection != 'q':
        print("\tType: ")
        print("\t\tp - to promote the employee")
        print("\t\td - to demote the employee")
        print("\t\tr - to raise the employee's salary by a given amount")
        print("\t\tv - to view the employee's details")
        print("\t\tq - to quit")
        print("\t\tf - to fire")
        print("\t\th - to hire\n")

        selection = input("\tEnter selection: ")[0]
        if selection == 'p':
            employee.promote()
        elif selection == 'd':
            employee.demote()
        elif selection == 'r':
            rise = int(input("\tEnter amount of rise: "))
            employee.raise_salary_by(rise)
        elif selection == 'v':
            print("\t" + employee.__str__())
        elif selection == 'f':
            employee.fire()
        elif selection == 'h':
            employee.hire()
    if employee == emp2 :
      print("Equal")
    else :
      print("Not equal")
    print("\tPROGRAM ENDED\n")

if __name__ == "__main__":
    main()

