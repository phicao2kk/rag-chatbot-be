from fastapi import APIRouter
from core.models import feedback

router = APIRouter(prefix="/feedback", tags=['feedback'])

@router.post("/submit")
def submit(
    payload: feedback.FeedbackSubmit
):
    # store payload onto mysql 
    
    return payload