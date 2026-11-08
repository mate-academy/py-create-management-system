import dataclasses
import datetime
import pickle


@dataclasses.dataclass
class Specialty:
    name: str
    number: int


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime.date
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list = dataclasses.field(default_factory=list)


def write_groups_information(groups: list[Group]) -> int:
    maximum_number_of_students = 0
    with open("groups.pickle", "wb") as file:
        for group in groups:
            if len(group.students) > maximum_number_of_students:
                maximum_number_of_students = len(group.students)
            pickle.dump(group, file)
    return maximum_number_of_students


def write_students_information(students: list[Student]) -> int:
    number_of_students = 0
    with open("students.pickle", "wb") as file:
        for student in students:
            number_of_students += 1
            pickle.dump(student, file)
    return number_of_students


def read_groups_information() -> set[str]:
    groups_speciality = set()
    with open("groups.pickle", "rb") as file:
        while True:
            try:
                item = pickle.load(file)
                groups_speciality.add(item.specialty.name)
            except EOFError:
                break
    return groups_speciality


def read_students_information() -> list[Student]:
    studentes_classes = []
    with open("students.pickle", "rb") as file:
        while True:
            try:
                item = pickle.load(file)
                studentes_classes.append(item)
            except EOFError:
                break
    return studentes_classes
