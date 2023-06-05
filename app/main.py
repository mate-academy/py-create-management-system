import dataclasses
from datetime import datetime
import pickle
from typing import Any
from typing import List


@dataclasses.dataclass
class Specialty:
    name: str
    number: int


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime.date
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: Any  # str or date
    students: List[Student]


spec_test = Specialty("Spec_name_1", 13)
stud_test = Student("Sanya", "Golova", "12.13.2022", 13.4, True,
                    "38021312", "Sanya street")
group_test = Group(spec_test, "14-gr", [stud_test])

print(spec_test)
print(spec_test)
print(group_test)


def write_groups_information(list_of_groups) -> int:
    with open("groups.pickle", "w"):
        pickle.dump(list_of_groups)


def write_students_information() -> None:
    pass


def read_groups_information() -> None:
    pass


def read_students_information() -> None:
    pass
