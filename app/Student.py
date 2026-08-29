from datetime import datetime
from dataclasses import dataclass


@dataclass
class Student:
    def __init__(self,
                 first_name: str,
                 last_name: str,
                 birth_date: datetime,
                 average_mark: float,
                 has_scholarship: bool,
                 phone_number: str,
                 address: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.average_mark = average_mark
        self.has_scholarship = has_scholarship
        self.phone_number = phone_number
        self.address = address
