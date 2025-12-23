from fastapi import APIRouter, HTTPException, Request
from backend.database import subscribers
from backend.functions import emailvalidation


router = APIRouter(prefix="/newsletter/subscribe")


@router.post("")
async def subscribe_newsletter(request: Request):
    data = await request.json()
    email = data.get("email")
    if emailvalidation.emailvalidation(email):
        return await subscribers.add_subscriber(email)
    else:
        raise HTTPException(status_code=400, detail="Invalid email address")
    
