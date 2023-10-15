from dataclasses import dataclass
# le module decoratrice des classes

@dataclass
class User:
    first_name: str
    age: int
    last_name: str=""

pat = User("pat", last_name="paat", age=10)
print(repr(pat))
# c'est égale à 
# class User:
#     def __init__(self, name, last_name) -> None:
#         self.name = name
#         self.last_name = last_name