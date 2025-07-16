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
    birth_date: int
    average_mark: float
    has_scholarship: True
    phone_number: str
    address: str


@dataclass
class Group:
    specialty : Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as pickle_file:
        pickle.dump(groups, pickle_file)
        if not groups:
            return 0
    return max(len(group.students) for group in groups)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        pickle.dump(students, pickle_file)
    return len(students)


def read_groups_information() -> any:
    with open("groups.pickle", "rb") as pickle_file:
        load_groups = pickle.load(pickle_file)
        sorted_spec = set()
        for i in load_groups:
            sorted_spec.add(i.specialty.name)
        return sorted_spec


def read_students_information() -> list:
    with open("students.pickle", "rb") as pickle_file:
        load_groups = pickle.load(pickle_file)
        class_obj = []
        for i in load_groups:
            class_obj.append(i)
        return class_obj
