from abc import ABC,abstractmethod
class Person(ABC):
    @abstractmethod
    def get_data(self,id,name,age):
        pass
    def display(self):
        pass
class Employee(Person):
    salary=50000
    def get_data(self, id, name, age):
        self.id=id
        self.name=name
        self.age=age
    def display(self):
        print("employee details:")
        print(f"id: {self.id} name: {self.name}  age: {self.age} salary: {self.salary}")
class Customer(Person):
     credit_rating=5
     def get_data(self, id, name, age):
        self.id=id
        self.name=name
        self.age=age
     def display(self):
         print("customer details:")
         print(f"id: {self.id} name:{self.name} age: {self.age} credit_rating: {self.credit_rating}")
emp=Employee()
cus=Customer()
emp.get_data(1,"arun kc",24)
cus.get_data(12,"roshan karki",25)
emp.display()
cus.display()

