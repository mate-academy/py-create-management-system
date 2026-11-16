import dataclasses
import pickle
from datetime import datetime


GROUPS_FILE_NAME = "groups.pickle"
STUDENTS_FILE_NAME = "students.pickle"


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
    with open(GROUPS_FILE_NAME, "wb") as groups_file:
        for group in groups:
            pickle.dump(group, groups_file)

        return max((len(group.students) for group in groups), default=0)


def write_students_information(students: list[Student]) -> int:
    with open(STUDENTS_FILE_NAME, "wb") as students_file:
        for student in students:
            pickle.dump(student, students_file)

    return len(students)


def read_all_objects(file_name: str) -> list:
    objects = []

    with open(file_name, "rb") as source_file:
        while True:
            try:
                objects.append(pickle.load(source_file))
            except EOFError:
                break

    return objects


def read_groups_information() -> list[str]:
    groups = read_all_objects(GROUPS_FILE_NAME)
    specialty_names = [group.specialty.name for group in groups]

    return list(dict.fromkeys(specialty_names))


def read_students_information() -> list[Student]:
    return read_all_objects(STUDENTS_FILE_NAME)
