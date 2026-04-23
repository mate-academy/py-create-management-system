from dataclasses import dataclass
from datetime import datetime
import pickle


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
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


# Function write all Group classes into file
def write_groups_information(groupes: list[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        max_students = 0
        for groupe in groupes:
            pickle.dump(groupe, file)
            if len(groupe.students) > max_students:
                max_students = len(groupe.students)
    return max_students


# Function write all Student classes into file
def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


# Function read Groups information from file and return specialties'
# names without repetition
def read_groups_information() -> str:
    all_specialtys = []
    with open("groups.pickle", "rb") as file:
        while True:
            try:
                group = pickle.load(file)
                all_specialtys.append(group.specialty.name)
            except EOFError:
                break
    return set(all_specialtys)


# Function return list of all the `Student` class instances.
def read_students_information() -> list:
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)
    return students
