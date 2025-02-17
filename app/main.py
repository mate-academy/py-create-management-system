import datetime
import pickle
from dataclasses import  dataclass
from datetime import datetime

@dataclass()
class Specialty:
    name: str
    number: int


@dataclass()
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: int
    score: int
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass()
class Group:
    specialty: Specialty
    course: int
    students: list[Student]
