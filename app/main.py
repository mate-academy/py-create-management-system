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


def read_all_from_pickle(filename: str) -> list:
    results = []
    with open(filename, "rb") as f:
        while True:
            try:
                results.append(pickle.load(f))
            except EOFError:
                break
    return results


def write_groups_information(groups: list[Group]) -> int:
    max_students = 0
    with open("groups.pickle", "wb") as file:
        for group in groups:
            pickle.dump(group, file)
            max_students = max(max_students, len(group.students))
    return max_students


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        for student in students:
            pickle.dump(student, file)
    return len(students)


def read_groups_information() -> list[str]:
    groups = read_all_from_pickle("groups.pickle")
    specialty_names = {group.specialty.name for group in groups}
    return list(specialty_names)


def read_students_information() -> list[Student]:
    return read_all_from_pickle("students.pickle")
