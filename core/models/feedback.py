from pydantic import BaseModel
from typing import Optional

class FeedbackSubmit(BaseModel):
    fullname: str
    phone: str
    field_id: int
    content: Optional[str]
