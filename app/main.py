# app/main.py
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Iterable, List
import pickle


# ======== Data models ========


@dataclass(slots=True)
class Specialty:
    name: str
    number: int


@dataclass(slots=True)
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass(slots=True)
class Group:
    specialty: Specialty
    course: int
    students: List[Student] = field(default_factory=list)


# ======== Persistence helpers ========

_GROUPS_FILE = "groups.pickle"
_STUDENTS_FILE = "students.pickle"


def _dump(obj: object, filename: str) -> None:
    """Write object with pickle using built-in open (so tests can patch)."""
    with open(
        filename,
        "wb",
    ) as f:  # noqa: PTH123
        pickle.dump(obj, f, protocol=pickle.HIGHEST_PROTOCOL)


def _load(filename: str) -> object:
    """Load object from pickle file using built-in open (tests can patch)."""
    with open(
        filename,
        "rb",
    ) as f:  # noqa: PTH123
        return pickle.load(f)


# ======== API required by the task ========

def write_groups_information(groups: Iterable[Group]) -> int:
    """
    Write all groups info into 'groups.pickle'.
    Return the maximum number of students among the groups.
    """
    groups_list = list(groups)
    _dump(groups_list, _GROUPS_FILE)

    return max((len(g.students) for g in groups_list), default=0)


def write_students_information(students: Iterable[Student]) -> int:
    """
    Write all students into 'students.pickle'.
    Return the number of students written.
    """
    students_list = list(students)
    _dump(students_list, _STUDENTS_FILE)

    return len(students_list)


def read_groups_information() -> List[str]:
    """
    Read 'groups.pickle' and return all specialties' names without repetition.
    """
    groups_list: List[Group] = _load(
        _GROUPS_FILE,
    )  # type: ignore[assignment]
    specialties = {g.specialty.name for g in groups_list}

    return list(specialties)


def read_students_information() -> List[Student]:
    """Read 'students.pickle' and return all Student instances."""
    students_list: List[Student] = _load(
        _STUDENTS_FILE,
    )  # type: ignore[assignment]

    return students_list
