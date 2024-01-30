# write your code here
import dataclasses
from datetime import datetime
import pickle
import os


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
    if not groups:
        return 0
    stud_list = []
    with open("groups.pickle", "wb") as file:
        for group in groups:
            stud_list.append(len(group.students))
            pickle.dump(group, file)
    return max(stud_list)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file_stud:
        pickle.dump(students, file_stud)
    return len(students)


def read_groups_information() -> list[str]:
    file_path = "groups.pickle"

    if not os.path.exists(file_path):
        return []

    unique_specialties = set()

    with open(file_path, "rb") as file:
        try:
            while True:
                group = pickle.load(file)
                unique_specialties.add(group.specialty.name)

        except EOFError:
            pass

    return list(unique_specialties)


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)
    return students
