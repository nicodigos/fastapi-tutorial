# Lesson: https://fastapi.tiangolo.com/python-types/#pydantic-models

from pydantic import BaseModel

def salute(salute:str, name:str) -> str:
    return salute + ' ' + name

def list_fruits(fruits: list[str]) -> None:
    for fruit in fruits:
        print(fruit.capitalize())

def union_types(number: int | float) -> int | float:
    return number

def dict_ages(people: dict[str, int] | None) -> None:
    if people is not None: 
        for k, v in people.items():
            print(k, v)

class Person:
    name: str
    age: int

    def __init__(self, name, age):
        self.name = name
        self.age = age

def person_function_call(person: Person) -> None:
    print(person.age)
    print(person.name)


class Agent(BaseModel):
    id: int
    assets: dict[str, int]
    money: int

    
print(salute('Hello', 'Nicolas'))
list_fruits(['banana', 'pineapple', 'orange'])
print(union_types(34))
print(union_types(34.0))
dict_ages({'Nicolas': 31, 'Tatiana': 28})

person = Person('Mila', 5)
person_function_call(person)

agent_comming_from_json = {
    'id': 12345,
    'assets': {'banana': 10, 'computer': 1, 'house': 0},
    'money': 1200
}

agent = Agent(**agent_comming_from_json)
print(agent.assets)

