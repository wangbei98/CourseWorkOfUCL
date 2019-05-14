###  This module defines a class that models an employee.
#


## An employee has a name and a salary.
#
class Employee:
    DEFAULT_STARTING_SALARY = 10000
    INCREMENT = 1000

    ## Constructs an Employee with a name and starting salary.
    #  @param employee_name the name of the employee.
    #
    def __init__(self, employee_name):
        self.name = employee_name
        self.salary = Employee.DEFAULT_STARTING_SALARY
        self.isHired = True

    ##
    # @return string representation of object.
    #
    def __str__(self):
        return "Name: " + self.name + ", salary: " + str(self.salary)

    ## name property allows get/set access to Employee's name value.
    #  name must not be whitespace else a ValueError is raised.
    #
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, theName):
        if len(theName.strip()) != 0:
            self._name = theName
        else:
            raise ValueError("Invalid name: " + self.name)

    ## salary property allows get/set access to Employee's salary.
    #  salary will be set to zero if there is an attempt to reduce
    #  it below zero.
    #
    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salaryAmount):
        if salaryAmount >= 0:
            self._salary = salaryAmount
        else:
            self._salary = 0

    ## Promotes the employee by increasing the salary by INCREMENT.
    #
    def promote(self):
        if self.isHired == False:
            print('cannot promote someone is unemployed')
            return
        self.salary += Employee.INCREMENT

    ## Demotes the employee by decreasing the salary by INCREMENT.
    #
    def demote(self):
        if self.isHired == False:
            print('cannot promote someone is unemployed')
            return
        self.salary -= Employee.INCREMENT

    ## Raises the salary of the employee by the amount passed as a parameter.
    # @param pay_rise the amount by which the the salary should be raised.
    #
    def raise_salary_by(self, pay_rise):
        self.salary += pay_rise

    ## Determines if this employee is equal to another employee.
    #  @param rhsValue the right-hand side employee.
    #  @return True if the names and the salaries are equal.
    #  @exception TypeError if the objects being compared are not
    #             the same type.
    #
    def __eq__(self, rhsValue):
        if isinstance(rhsValue, Employee):
            return (self.name == rhsValue.name and
                    self.salary == rhsValue.salary)
        else:
            raise TypeError("Argument must be an Employee object.")

    def getIsHired(self):
        return self.isHired
    def setIsHired(self,isHired):
        if isHired:
            self.isHired = isHired
            self.salary = self.DEFAULT_STARTING_SALARY
        else:
            self.isHired = isHired
            self.salary = 0
    def IsHired(self):
        return self.isHired

    ## hire()
    def hire(self):
        self.isHired = True
        self.salary = self.DEFAULT_STARTING_SALARY

    ## fire()

    def fire(self):
        self.isHired = False
        self.salary = 0


