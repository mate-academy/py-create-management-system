import dataclasses
import pickle


@dataclasses.dataclass
class Specialty:
    name: str
    number: int


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: str
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as pickle_file:
        pickle.dump(groups, pickle_file)
    if not groups:
        return 0
    max_students = max(len(group.students) for group in groups)
    return\
        max_students


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        pickle.dump(students, pickle_file)
    return len(students)


def read_groups_information(file_name: str = "groups.pickle") -> list:
    with open(f"{file_name}", "rb") as pickle_file:
        groups = pickle.load(pickle_file)
        specialties = set()
        for group in groups:
            specialties.add(group.specialty.name)
        return list(specialties)


def read_students_information(file_name: str = "students.pickle") -> list:
    with open(file_name, "rb") as pickle_file:
        students = pickle.load(pickle_file)
        return students
