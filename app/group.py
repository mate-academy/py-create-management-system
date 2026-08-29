import dataclasses

from app.specialty import Specialty
from app.student import Student


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]
