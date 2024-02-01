import dataclasses
import os
import pickle


@dataclasses.dataclass
class Specialty:
    name: str
    number: int


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: str
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: "Specialty"
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    if not groups:
        return 0
    max_students = max(len(group.students) for group in groups)
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)
    return max_students


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information() -> list[str]:
    specialties = set()
    if os.path.exists("groups.pickle"):
        with open("groups.pickle", "rb") as file:
            groups = pickle.load(file)
            for group in groups:
                specialties.add(group.specialty.name)
        return list(specialties)
    return []


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)
    return students
