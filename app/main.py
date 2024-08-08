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
    has_scholarship: float
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: str
    students: list[Student]


def write_groups_information(lyceum_groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(lyceum_groups, file)
    the_most_students = 0
    for group in lyceum_groups:
        if len(group.students) > the_most_students:
            the_most_students = len(group.students)
    return the_most_students


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as file:
        read_data = pickle.load(file)
    specialty_list = []
    for group in read_data:
        if group.specialty.name not in specialty_list:
            specialty_list.append(group.specialty.name)

    return specialty_list


def read_students_information() -> list:
    with open("students.pickle", "rb") as file:
        read_data = pickle.load(file)
    return read_data
