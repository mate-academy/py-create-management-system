from dataclasses import dataclass
import pickle


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: str
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    res = []
    to_dump = []
    with open("groups.pickle", "wb") as file:
        for group in groups:
            res.append(len(group.students))
            to_dump.append(group)
        pickle.dump(to_dump, file)
    return max(res) if len(res) > 0 else 0


def write_students_information(students: list[Student]) -> int:
    to_dump = []
    with open("students.pickle", "wb") as file:
        for student in students:
            to_dump.append(student)
        pickle.dump(to_dump, file)
    return len(students)


def read_groups_information() -> list:
    res = set()
    with open("groups.pickle", "rb") as file:
        data_from_file = pickle.load(file)
        for i in data_from_file:
            res.add(i.specialty.name)
    return list(res)


def read_students_information() -> list:
    with open("students.pickle", "rb") as file:
        res = pickle.load(file)
    return res
