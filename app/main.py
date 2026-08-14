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
    return max((len(group.students) for group in groups), default=0)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information() -> list[str]:
    speciality_names = []
    with open("groups.pickle", "rb") as file:
        while True:
            try:
                data = pickle.load(file)
                if isinstance(data, list):
                    for group in data:
                        name = group.specialty.name
                        if name not in speciality_names:
                            speciality_names.append(name)
                else:
                    name = group.specialty.name
                    if name not in speciality_names:
                        speciality_names.append(name)
            except EOFError:
                break
    return speciality_names


def read_students_information() -> list[Student]:
    students = []
    with open("students.pickle", "rb") as file:
        while True:
            try:
                data = pickle.load(file)
                if isinstance(data, list):
                    students.extend(data)
                else:
                    students.append(data)
            except EOFError:
                break
    return students
