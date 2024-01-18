import pickle
from dataclasses import dataclass


@dataclass
class Specialty:
    name: str
    number: int
    pass


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: str
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str
    pass


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    if not groups:
        return 0
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)
    return max(len(group.students) for group in groups)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information() -> list:
    specialties = set()
    try:
        try:
            with open("groups.pickle", "rb") as file:
                groups = pickle.load(file)
                for group in groups:
                    specialties.add(group.specialty.name)
        except EOFError:
            return []
    except FileNotFoundError:
        print(f"""No such file {"groups.pickle"}""")
    return list(specialties)


def read_students_information() -> list:
    try:
        try:
            with open("students.pickle", "rb") as file:
                students = pickle.load(file)
                return students
        except EOFError:
            return []
    except FileNotFoundError:
        print(f"""No such file {"students.pickle"}""")
