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
    course: int | str
    students: list

def write_groups_information(groups: list[Group]) -> int:
    if not groups:
        return 0
    max_students = max(len(group.students) for group in groups)
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)
    return max_students



def write_students_information(students: list[Student]) -> int:
    num_students = len(students)
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return num_students


def read_groups_information() -> set:
    specialties = set()
    try:
        with open("groups.pickle", "rb") as file:
            groups = pickle.load(file)
            for group in groups:
                specialties.add(group.specialty.name)
    except FileNotFoundError:
        pass  # Return an empty list of specialties if the file doesn't exist
    return list(specialties)


def read_students_information() -> str:
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)
    return students
