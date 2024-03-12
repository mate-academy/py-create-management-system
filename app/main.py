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
    students: list


def write_groups_information(groups):
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)
    return max(len(group.students) for group in groups)


def write_students_information(students):
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information():
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)
    return list(set(group.specialty.name for group in groups))

а
def read_students_information():
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)
    return students
