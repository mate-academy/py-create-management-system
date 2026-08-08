import dataclasses
from datetime import datetime
from typing import List
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
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(list_group: List[Group]) -> int:
    if not list_group:
        with open("groups.pickle", "wb") as file_group:
            pickle.dump(list_group, file_group)
        return 0

    list_number_students = []
    with open("groups.pickle", "wb") as file_group:
        pickle.dump(list_group, file_group)

    for group in list_group:
        list_number_students.append(len(group.students))

    return max(list_number_students)


def write_students_information(list_students: List[Student]) -> int:
    with open("students.pickle", "wb") as file_students:
        pickle.dump(list_students, file_students)

    return len(list_students)


def read_groups_information() -> List[str]:

    list_specialty = []
    with open("groups.pickle", "rb") as file_name_specialty:
        groups = pickle.load(file_name_specialty)
        for group in groups:
            list_specialty.append(group.specialty.name)

    return list(set(list_specialty))


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as file_all_student:
        students = pickle.load(file_all_student)

    return list(students)
