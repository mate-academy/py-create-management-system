from dataclasses import dataclass
import pickle


@dataclass()
class Specialty:
    name: str
    number: int


@dataclass()
class Student:
    first_name: str
    last_name: str
    birth_date: str
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass()
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(list_group: list[Group]) -> int:
    quantity_of_students = 0
    for group in list_group:
        if quantity_of_students < len(group.students):
            quantity_of_students = len(group.students)

    with open("groups.pickle", "wb") as pickle_file:
        pickle.dump(list_group, pickle_file)

    return quantity_of_students


def write_students_information(list_of_students: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        pickle.dump(list_of_students, pickle_file)

    return len(list_of_students)


def read_groups_information(file_groups: str = "groups.pickle") -> set:
    names_of_groups = set()
    with open(file_groups, "rb") as pickle_file:
        groups = pickle.load(pickle_file)
        for group in groups:
            names_of_groups.add(group.specialty.name)

    return names_of_groups


def read_students_information(
        file_students: str = "students.pickle"
) -> list[Student]:
    students = []
    with open(file_students, "rb") as pickle_file:
        students = pickle.load(pickle_file)
    return students
