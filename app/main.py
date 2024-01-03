import pickle
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(
        input_data: list[Group]
) -> int:
    with open("groups.pickle", "wb") as output:
        for group in input_data:
            pickle.dump(group, output)
    return max([len(group.students) for group in input_data]) \
        if len([len(group.students) for group in input_data]) > 0 \
        else []


def write_students_information(
        input_data: list[Student]
) -> int:
    with open("students.pickle", "wb") as output:
        for group in input_data:
            pickle.dump(group, output)
    return len(input_data)


def read_groups_information(
        file_path: str = "groups.pickle"
) -> list[str]:
    objects = []
    with open(file_path, "rb") as input_file:
        while True:
            try:
                objects.append(pickle.load(input_file))
            except EOFError:
                # Reached the end of the file
                break
    return list(set([group.specialty.name for group in objects]))


def read_students_information(
        file_path: str = "students.pickle"
) -> list[Student]:
    objects = []
    with open(file_path, "rb") as input_file:
        while True:
            try:
                objects.append(pickle.load(input_file))
            except EOFError:
                break
    return objects
