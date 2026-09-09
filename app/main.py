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
    average_mark: float | int
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list


def write_groups_information(groups: list[Group]) -> int:
    max_students = max((len(group.students) for group in groups), default=0)
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)
    return max_students


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information() -> set[str]:
    with open("groups.pickle", "rb") as file:
        loaded_groups = pickle.load(file)
    unique_names = set()
    for group in loaded_groups:
        unique_names.add(group.specialty.name)
    return unique_names


def read_students_information() -> set[str]:
    with open("students.pickle", "rb") as file:
        student_list = pickle.load(file)
    return student_list
