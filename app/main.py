from __future__ import annotations

import dataclasses
import pickle
from datetime import datetime
from typing import List, Set


@dataclasses.dataclass
class Specialty:
    name: str
    number: int


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student] = dataclasses.field(default_factory=list)


def write_groups_information(groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as file_obj:
        for group in groups:
            pickle.dump(group, file_obj, protocol=pickle.HIGHEST_PROTOCOL)

    return max((len(group.students) for group in groups), default=0)


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as file_obj:
        for student in students:
            pickle.dump(student, file_obj, protocol=pickle.HIGHEST_PROTOCOL)

    return len(students)


def read_groups_information() -> Set[str]:
    specialties: Set[str] = set()

    try:
        with open("groups.pickle", "rb") as file_obj:
            while True:
                loaded = pickle.load(file_obj)

                if isinstance(loaded, Group):
                    specialties.add(loaded.specialty.name)
                    continue

                try:
                    for group in loaded:
                        if isinstance(group, Group):
                            specialties.add(group.specialty.name)
                except TypeError:
                    pass

    except FileNotFoundError:
        return set()
    except EOFError:
        pass

    return specialties


def read_students_information() -> List[Student]:
    students: List[Student] = []

    try:
        with open("students.pickle", "rb") as file_obj:
            while True:
                loaded = pickle.load(file_obj)

                if isinstance(loaded, Student):
                    students.append(loaded)
                    continue

                try:
                    for item in loaded:
                        if isinstance(item, Student):
                            students.append(item)
                except TypeError:
                    pass

    except FileNotFoundError:
        return []
    except EOFError:
        pass

    return students
