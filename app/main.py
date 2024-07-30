import dataclasses
import pickle
from datetime import datetime



@dataclasses.dataclass
class Specialty:
    name: str
    number: int


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Croup:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(input: list) -> int:
    with open("group.pickle", "wb") as file:
        pickle.dump(input, file)
    return max([len(input[n].students) for n in input])





