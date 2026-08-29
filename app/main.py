import dataclasses
from datetime import datetime
import pickle


# Specialty class
@dataclasses.dataclass
class Specialty:
    name: str
    number: int


# Student class
@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


# Group class
@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list


# Function to write groups information to a file
def write_groups_information(groups: list) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)

    # Handle the case where the list of groups is empty
    if not groups:
        return 0

    # Find the group with the maximum number of students
    max_students = max(len(group.students) for group in groups)
    return max_students


# Function to write students information to a file
def write_students_information(students: list) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)

    # Return the number of students stored
    return len(students)


# Function to read groups information from the file
def read_groups_information() -> list:
    try:
        with open("groups.pickle", "rb") as file:
            groups = pickle.load(file)
            specialty_names = {group.specialty.name for group in groups}
            return list(specialty_names)
    except FileNotFoundError:
        return []


# Function to read students information from the file
def read_students_information() -> list:
    try:
        with open("students.pickle", "rb") as file:
            students = pickle.load(file)
            return students
    except FileNotFoundError:
        return []
