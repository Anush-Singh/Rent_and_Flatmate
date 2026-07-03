from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.listing import Listing

router = APIRouter(
    prefix="/search",
    tags=["Search"]
)


@router.get("/")
def search(
    city: str,
    db: Session = Depends(get_db)
):
    listings = db.query(Listing).filter(
        Listing.location.ilike(f"%{city}%")
    ).all()

    return listings