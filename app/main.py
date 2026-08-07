from datetime import datetime
import dataclasses
import pickle


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
    phone_number: int
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)
    number_of_students = 0
    for group in groups:
        number_of_students = (max(number_of_students, len(group.students)))
    return number_of_students


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information() -> list:
    specialities = []
    with open("groups.pickle", "rb") as file:
        src = pickle.load(file)

        for group in src:
            if group.specialty.name not in specialities:
                specialities.append(group.specialty.name)
    return specialities


def read_students_information() -> list:
    with open("students.pickle", "rb") as file:
        src = list(pickle.load(file))
        return src
