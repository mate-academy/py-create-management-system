from dataclasses import dataclass
from typing import List
from app.Specialty import Specialty
from app.Student import Student


@dataclass
class Group:
    specialty: Specialty
    course : float
    students : List[Student]
