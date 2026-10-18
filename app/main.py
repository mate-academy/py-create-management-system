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
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)
    students_quantity = []
    for group in groups:
        students_quantity.append(len(group.students))
    if len(students_quantity) > 0:
        return max(students_quantity)
    else:
        return 0


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)
        list_of_specialties = []
        for group in groups:
            if group.specialty.name in list_of_specialties:
                continue
            else:
                list_of_specialties.append(group.specialty.name)
        print(list_of_specialties)
        return list_of_specialties


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)
    print(students)
    return students
