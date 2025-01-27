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
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(data: list[Group]) -> int:
    with open(r"groups.pickle", "wb") as source_file:
        pickle.dump(data, source_file)
    if data:
        return max(len(group.students) for group in data)
    else:
        return 0


def write_students_information(data: list[Student]) -> int:
    with open(r"students.pickle", "wb") as source_file:
        pickle.dump(data, source_file)
    result = 0
    for student in data:
        if isinstance(student, Student):
            result += 1
    return result


def read_groups_information(file_name: str = "groups.pickle") -> list[str]:
    with open(file_name, "rb") as source_file:
        data = pickle.load(source_file)
    specialties = {group.specialty.name for group in data}
    return list(specialties)


def read_students_information(
        file_name: str = "students.pickle"
) -> list[Student]:
    with open(file_name, "rb") as source_file:
        data = pickle.load(source_file)
    return data
