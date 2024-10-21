import dataclasses
from datetime import datetime
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
    groups_count = []
    with open("groups.pickle", "wb") as f:
        for group in groups:
            pickle.dump(group, f)
            groups_count.append(len(group.students))

    if not groups_count:
        return 0

    return max(groups_count)


def write_students_information(students: list[Student]) -> int:
    students_count = 0
    with open("students.pickle", "wb") as f:
        for student in students:
            pickle.dump(student, f)
            students_count += 1

    return students_count


def read_groups_information() -> list:
    groups_list = []
    with open("groups.pickle", "rb") as f:
        # groups_list.append(pickle.load(f))
        while True:
            try:
                groups_list.append(pickle.load(f))
            except EOFError:
                break

    lst = []
    for group in groups_list:
        lst.append(group.specialty.name)

    return list(set(lst))


def read_students_information() -> list:
    students_list = []
    with open("students.pickle", "rb") as f:
        # students_list.append(pickle.load(f))
        while True:
            try:
                students_list.append(pickle.load(f))
            except EOFError:
                break

    return students_list
