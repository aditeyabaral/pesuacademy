"""Model for TimeTable in the PESU Academy system."""

from pydantic import BaseModel


class ClassSession(BaseModel):
    """Represents a single class session at a specific time.

    Attributes:
        course_code (str): The code of the subject.
        course_name (str): The name of the subject.
        teacher (str): The name of the teacher for the class.
    """

    code: str
    name: str
    teacher: str


class TimeSlot(BaseModel):
    """Represents a single row in the timetable (e.g., 8:00 AM - 8:45 AM).

    Attributes:
        time (str): The time slot for the class (e.g., "8:00 AM - 8:45 AM").
        is_break (bool): Indicates if this time slot is a break.
        monday (Optional[ClassSession]): Class session on Monday, if any.
        tuesday (Optional[ClassSession]): Class session on Tuesday, if any.
        wednesday (Optional[ClassSession]): Class session on Wednesday, if any.
        thursday (Optional[ClassSession]): Class session on Thursday, if any.
        friday (Optional[ClassSession]): Class session on Friday, if any.
        saturday (Optional[ClassSession]): Class session on Saturday, if any.
    """

    time: str
    is_break: bool = False
    monday: ClassSession | None = None
    tuesday: ClassSession | None = None
    wednesday: ClassSession | None = None
    thursday: ClassSession | None = None
    friday: ClassSession | None = None
    saturday: ClassSession | None = None


class Timetable(BaseModel):
    """The main model to hold the entire weekly schedule.

    Attributes:
        time_slots (List[TimeSlot]): A list of time slots representing the weekly schedule.
    """

    time_slots: list[TimeSlot]
