import dataclasses
from datetime import datetime
import pickle


@dataclasses.dataclass
class Specialty:
    name: str
    number: str


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
    course: str
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)

    max_students = 0
    if groups:
        for group in groups:
            if len(group.students) > max_students:
                max_students = len(group.students)
    return max_students


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)
    return len(students)


def read_groups_information() -> set[str]:
    try:
        with open("groups.pickle", "rb") as f:
            groups: list[Group] = pickle.load(f)
    except FileNotFoundError:
        print("Error: 'groups.pickle' not found.")
        return set()
    except Exception as e:
        print(f"An error occurred while reading 'groups.pickle': {e}")
        return set()

    specialty_names = set()
    for group in groups:
        specialty_names.add(group.specialty.name)
    return specialty_names


def read_students_information() -> list[Student]:
    try:
        with open("students.pickle", "rb") as f:
            students: list[Student] = pickle.load(f)
        return students
    except FileNotFoundError:
        print("Error: 'students.pickle' not found.")
        return []
    except Exception as e:
        print(f"An error occurred while reading 'students.pickle': {e}")
        return []
