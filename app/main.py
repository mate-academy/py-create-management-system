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
    birth_date: int
    average_mark: float
    has_scholarship: bool
    phone_number: int
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(input_info: str) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(input_info, file)
        for group in input_info:
            return len(group.students)


def write_students_information(input_info2: str) -> int:
    with open("students.pickle", "wb") as file2:
        pickle.dump(input_info2, file2)
        return len(input_info2)


def read_groups_information() -> set:
    result = set()
    with open("groups.pickle", "rb") as file_read:
        for out_file in pickle.load(file_read):
            result.add(out_file.specialty.name)
        return result


def read_students_information() -> str:
    with open("students.pickle", "rb") as file2_read:
        out_file = pickle.load(file2_read)
        return out_file
