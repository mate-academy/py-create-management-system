from typing import List
from dataclasses import dataclass
from app.Specialty import Specialty
from app.Student import Student


@dataclass
class Group:
    def __init__(self,
                 specialty: Specialty,
                 course: int,
                 students: List[Student]) -> None:
        self.specialty = specialty
        self.course = course
        self.students = students
