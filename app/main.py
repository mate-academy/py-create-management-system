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
    birth_date: int
    average_mark: float
    has_scholarship: bool
    phone_number: int
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    max_students = 0
    with open("groups.pickle", "wb") as file:
        for group in groups:
            pickle.dump(group, file)
            if len(group.students) > max_students:
                max_students = len(group.students)
    return max_students


def write_students_information(students: list[Student]) -> int:
    count_students = 0
    with open("students.pickle", "wb") as file:
        for student in students:
            pickle.dump(student, file)
            count_students += 1
    return count_students


def read_groups_information() -> list:
    specialties = set()

    with open("groups.pickle", "rb") as file:
        try:
            while True:
                group = pickle.load(file)
                specialties.add(group.specialty.name)
        except EOFError:
            pass
    return list(specialties)


def read_students_information() -> list[Student]:
    list_students = []
    with open("students.pickle", "rb") as file:
        try:
            while True:
                list_students.append(pickle.load(file))
        except EOFError:
            pass
    return list_students
