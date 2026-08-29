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


def write_info(file_name: str, elements: list) -> list:
    result_list = []

    with open(file_name, "wb") as file_to_write:
        for element in elements:
            pickle.dump(element, file_to_write)
            result_list.append(element)

    return result_list


def read_info(file_name: str) -> list:
    result_list = []

    with open(file_name, "rb") as file_to_read:
        while True:
            try:
                result_list.append(
                    pickle.load(file_to_read)
                )
            except EOFError:
                break

    return result_list


def write_groups_information(groups: list[Group]) -> int:
    write_info("groups.pickle", groups)
    return (
        max(
            len(group.students)
            for group in groups
        )
        if groups
        else 0
    )


def write_students_information(students: list[Student]) -> int:
    return len(write_info("students.pickle", students))


def read_groups_information() -> list:
    return list(set(
        group.specialty.name
        for group in read_info("groups.pickle")
    ))


def read_students_information() -> list:
    return read_info("students.pickle")
