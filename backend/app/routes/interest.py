from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.interest import InterestRequest
from app.schemas.interest import InterestCreate

router = APIRouter(prefix="/interest", tags=["Interest"])


@router.post("/")
def send_interest(data: InterestCreate, db: Session = Depends(get_db)):
    request = InterestRequest(
        tenant_id=data.tenant_id,
        listing_id=data.listing_id,
        status="Pending"
    )

    db.add(request)
    db.commit()

    return {"message": "Interest request sent"}


@router.get("/")
def get_requests(db: Session = Depends(get_db)):
    return db.query(InterestRequest).all()


# -------------------------
# Accept Request
# -------------------------
@router.put("/{request_id}/accept")
def accept_request(request_id: int, db: Session = Depends(get_db)):
    request = db.query(InterestRequest).filter(
        InterestRequest.id == request_id
    ).first()

    if request is None:
        return {"message": "Request not found"}

    request.status = "Accepted"
    db.commit()

    return {"message": "Accepted"}


# -------------------------
# Reject Request
# -------------------------
@router.put("/{request_id}/reject")
def reject_request(request_id: int, db: Session = Depends(get_db)):
    request = db.query(InterestRequest).filter(
        InterestRequest.id == request_id
    ).first()

    if request is None:
        return {"message": "Request not found"}

    request.status = "Rejected"
    db.commit()

    return {"message": "Rejected"}