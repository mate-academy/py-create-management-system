import dataclasses
from datetime import datetime
from pickle import dump, load


@dataclasses.dataclass()
class Specialty:
    name: str
    number: int


@dataclasses.dataclass()
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass()
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(group_list: list[Group]) -> int:
    with open("groups.pickle", "wb") as file_to_write:
        dump(group_list, file_to_write)
    if not group_list:
        return 0
    return max(len(group.students) for group in group_list)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file_to_write:
        dump(students, file_to_write)
    return len(students)


def read_groups_information() -> list[str]:
    with open("groups.pickle", "br") as file_to_read:
        groups = load(file_to_read)
        specialty_names = dict()
        for group in groups:
            specialty_names.update({group.specialty.name: ""})
        return list(specialty_names.keys())


def read_students_information() -> list[Student]:
    with open("students.pickle", "br") as file_to_read:
        return load(file_to_read)
