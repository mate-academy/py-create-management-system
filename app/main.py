from dataclasses import dataclass
from datetime import date
import pickle
from typing import List


# Define Specialty class
@dataclass
class Specialty:
    name: str
    number: int


# Define Student class
@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: date
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


# Define Group class
@dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    if not groups:
        with open("groups.pickle", "wb") as file:
            pickle.dump(groups, file)
        return 0  # Return 0 when groups list is empty

    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)

    max_students = max(len(group.students) for group in groups)
    return max_students


# Function to write students information to "students.pickle"
def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)

    return len(students)


# Function to read groups information from "groups.pickle"
def read_groups_information() -> List[str]:
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)

    specialties = set(group.specialty.name for group in groups)
    return list(specialties)


# Function to read students information from "students.pickle"
def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)

    return students
