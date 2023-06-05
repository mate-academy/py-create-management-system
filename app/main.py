import dataclasses
from datetime import datetime
import pickle
from typing import Any
from typing import List


@dataclasses.dataclass
class Specialty:
    name: str
    number: int


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime.date
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: Any  # str or date
    students: List[Student]


def write_groups_information(list_of_groups: list[Group]) -> int:
    stud_counter = 0
    for i in list_of_groups:
        if len(i.students) > stud_counter:
            stud_counter = len(i.students)
    with open("groups.pickle", "wb") as f:
        pickle.dump(list_of_groups, f)
    return stud_counter


def write_students_information(list_of_students: list[Student]) -> None:
    with open("students.pickle", "wb") as f:
        pickle.dump(list_of_students, f)
    return len(list_of_students)


def read_groups_information() -> list:
    result = []
    with open("groups.pickle", "rb") as f:
        for i in pickle.load(f):
            result.append(i.specialty.name)

    return list(set(result))


def read_students_information() -> List[Student]:
    result = []
    with open("students.pickle", "rb") as f:
        for i in pickle.load(f):
            result.append(i)
    return result


if __name__ == "__main__":
    spec_test = Specialty("Spec_name_1", 13)
    spec_test_2 = Specialty("Spec_name_2", 23)

    stud_test = Student("Sanya", "Golova", "12.13.2022", 13.4, True,
                        "38021312", "Sanya street")
    stud_test_2 = Student("Vanya", "Dvauha", "12.13.2022", 26.32, True,
                          "38021312", "Vanya street")
    group_test = Group(spec_test, "14-gr", [stud_test, stud_test_2])
    group_test_2 = Group(spec_test_2, "15-gr", [stud_test_2])

    write_groups_information([group_test, group_test, group_test_2])
    write_students_information([stud_test, stud_test_2])
    read_groups_information()
    read_students_information()
