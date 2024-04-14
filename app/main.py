import dataclasses
import pickle

from datetime import datetime


class Specialty:
    def __init__(self, name: str, number: int) -> None:
        self.name = name
        self.number = number


class Student:
    def __init__(
            self,
            first_name: str,
            last_name: str,
            birth_date,
            average_mark: float,
            has_scholarship: bool,
            phone_number,
            address: str
    ) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.average_mark = average_mark
        self.has_scholarship = has_scholarship
        self.phone_number = phone_number
        self.address = address


class Group:
    def __init__(self, specialty: Specialty, course: int, students: list[Student]) -> None:
        self.specialty = specialty
        self.course = course
        self.students = students


