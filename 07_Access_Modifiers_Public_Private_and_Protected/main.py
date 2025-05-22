class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn

    def get_ssn(self):
        return self.__ssn

emp = Employee("Asad", 50000, "123-45-6789")
print(emp.get_ssn())  # Accessing private attribute through a method
print(emp.name)  # Public attribute
print(emp._salary)  # Protected attribute
