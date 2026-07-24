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
    birth_date: datetime.date
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups_list: list[Group]) -> int:
    with open("groups.pickle", "wb") as new_file:
        pickle.dump(groups_list, new_file)

    if not groups_list:
        return 0

    return max(len(group.students) for group in groups_list)


def write_students_information(students_list: list[Student]) -> int:
    with open("students.pickle", "wb") as new_file:
        pickle.dump(students_list, new_file)

    return len(students_list)


def read_groups_information() -> list:
    result = []
    with open("groups.pickle", "rb") as read_file:
        while True:
            try:
                groups = pickle.load(read_file)
                if isinstance(groups, list):
                    for group in groups:
                        if group.specialty.name not in result:
                            result.append(group.specialty.name)
                else:
                    if groups.specialty.name not in result:
                        result.append(groups.specialty.name)
            except EOFError:
                break

    return result


def read_students_information() -> list:
    with open("students.pickle", "rb") as read_file:
        return pickle.load(read_file)
