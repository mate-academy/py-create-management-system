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
    phone_number: int
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(list_of_groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(list_of_groups, file)
    return max(
        [len(group.students) for group in list_of_groups]
    ) if list_of_groups != [] else 0


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information() -> set:
    specialities = set()
    with open("groups.pickle", "rb") as file:
        while True:
            try:
                group = pickle.load(file)
                for student in group:
                    specialities.add(student.specialty.name)
            except EOFError:
                break
    return specialities


def read_students_information() -> list:
    list_of_students = []
    with open("students.pickle", "rb") as file:
        while True:
            try:
                group = pickle.load(file)
                list_of_students.extend(group)
            except EOFError:
                break
    return list_of_students
