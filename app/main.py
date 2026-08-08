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
    course: str
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as p_groups:
        pickle.dump(groups, p_groups)
    return max(len(group.students) for group in groups) if groups else None


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as p_students:
        pickle.dump(students, p_students)
    return len(students)


def read_groups_information() -> list[str]:
    with open("groups.pickle", "rb") as file:
        groups_list = pickle.load(file)
        result = []
        for group in groups_list:
            if group.specialty.name not in result:
                result.append(group.specialty.name)
        return result


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as file:
        return pickle.load(file)
