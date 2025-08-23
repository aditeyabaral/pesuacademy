"""Model for TimeTable in the PESU Academy system."""

from pydantic import BaseModel


class ClassSession(BaseModel):
    """Represents a single class session at a specific time.

    Attributes:
        code (str): The code of the course.
        name (str): The name of the course.
        teacher (str): The name of the teacher for the class.
    """

    code: str
    name: str
    teacher: str


class Slot(BaseModel):
    """Represents a single Slot in the timetable (e.g., 8:00 AM - 8:45 AM).

    Attributes:
        time (str): The time of the slot (e.g., 8:00 AM - 8:45 AM).
        is_break (bool): True if this is a break slot, False otherwise.
        session (Optional[ClassSession]): The class session for this slot, if any.
    """

    time: str
    is_break: bool = False
    session: ClassSession | None = None


class Timetable(BaseModel):
    """The main model to hold the entire weekly schedule.

    Attributes:
        monday (List[Slot]): The schedule for Monday.
        tuesday (List[Slot]): The schedule for Tuesday.
        wednesday (List[Slot]): The schedule for Wednesday.
        thursday (List[Slot]): The schedule for Thursday.
        friday (List[Slot]): The schedule for Friday.
        saturday (List[Slot]): The schedule for Saturday.
    """

    monday: list[Slot]
    tuesday: list[Slot]
    wednesday: list[Slot]
    thursday: list[Slot]
    friday: list[Slot]
    saturday: list[Slot]
