from dataclasses import dataclass


@dataclass
class User:
    f_name: str
    l_name: str
    email: str
    age: int
    salary: int
    dept: str
