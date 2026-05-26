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


def write_groups_information(groups: list[Group]) -> None:
    with open("groups.pickle", "wb") as pickle_file:
        pickle.dump(groups, pickle_file)

    if not groups:
        return 0

    return max(len(group.students) for group in groups)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        pickle.dump(students, pickle_file)

    return len(students)


def read_groups_information() -> list:
    try:
        with open("groups.pickle", "rb") as file:
            groups = pickle.load(file)
    except (FileNotFoundError, EOFError):
        return []
    return list({group.specialty.name for group in groups})


def read_students_information() -> list:
    try:
        with open("students.pickle", "rb") as file:
            data = pickle.load(file)
            if isinstance(data, list):
                return data
            return [data]
    except FileNotFoundError:
        return []
