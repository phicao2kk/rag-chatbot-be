
from pydantic import BaseModel


class FeedbackSubmit(BaseModel):
    fullname: str
    phone: str
    field_id: int
    content: str | None
