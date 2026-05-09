from typing import TypedDict

class Person(TypedDict):
    name:str
    age:int


person1: Person={'name':'raju','age':22}

print(person1)