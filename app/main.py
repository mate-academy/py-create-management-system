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


def write_groups_information(groups_list: list[Group]) -> int:
    with open("groups.pickle", "wb") as pickle_file:
        pickle.dump(groups_list, pickle_file)
    return max([len(group.students) for group in groups_list])\
        if groups_list else 0


def write_students_information(students_list: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        pickle.dump(students_list, pickle_file)
    return len(students_list)


def read_groups_information() -> list[str]:
    specialties = set()
    with open("groups.pickle", "rb") as pickle_file:
        result_list = pickle.load(pickle_file)
        for group in result_list:
            specialties.add(group.specialty.name)
    return list(specialties)


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as pickle_file:
        result_list = pickle.load(pickle_file)
    return result_list
