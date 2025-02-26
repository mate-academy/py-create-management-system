import pickle
from datetime import datetime
import dataclasses


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


def write_groups_information(groups):
    max_number = max(len(group.students) for group in groups) if groups else []

    try:
        with open("groups.pickle", "wb") as f:
            pickle.dump(groups, f)
    except Exception as e:
        print("Error occurs when write to file", e)
    return max_number


def write_students_information(students):
    try:
        with open("students.pickle", "wb") as file:
            pickle.dump(students, file)
    except Exception as e:
        print("Error occurs", e)
    return len(students)


def read_groups_information():
    try:
        with open("groups.pickle", "rb") as f:
            specialties_groups = pickle.load(f)
            specialty_name = set(group.specialty.name for group in specialties_groups)
            return specialty_name
    except Exception as e:
        print("Error occur when read file: ", e)
        return set()


def read_students_information():
    try:
        with open("students.pickle", "rb") as file:
            instances = pickle.load(file)
            return instances
    except Exception as e:
        print("Error occur when read file: ", e)
        return []
