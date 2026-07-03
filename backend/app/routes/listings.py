from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.listing import ListingCreate
from app.models.listing import Listing
from app.db.session import get_db

router = APIRouter(prefix="/listings", tags=["Listings"])


@router.post("/")
def create_listing(data: ListingCreate, db: Session = Depends(get_db)):
    new_listing = Listing(
        owner_id=data.owner_id,
        location=data.location,
        rent=data.rent,
        available_from=data.available_from,
        room_type=data.room_type,
        furnishing_status=data.furnishing_status
    )

    db.add(new_listing)
    db.commit()

    return {"message": "Listing created successfully"}


@router.get("/")
def get_listings(db: Session = Depends(get_db)):
    listings = db.query(Listing).all()

    result = []
    for item in listings:
        result.append({
            "id": item.id,
            "location": item.location,
            "rent": item.rent,
            "room_type": item.room_type
        })

    return result

from fastapi import HTTPException

@router.get("/{listing_id}")
def get_listing(listing_id: int, db: Session = Depends(get_db)):
    listing = db.query(Listing).filter(
        Listing.id == listing_id
    ).first()

    if not listing:
        raise HTTPException(status_code=404, detail="Listing not found")

    return listing


@router.put("/{listing_id}")
def update_listing(
    listing_id: int,
    data: ListingCreate,
    db: Session = Depends(get_db)
):
    listing = db.query(Listing).filter(
        Listing.id == listing_id
    ).first()

    if not listing:
        raise HTTPException(status_code=404, detail="Listing not found")

    listing.location = data.location
    listing.rent = data.rent
    listing.room_type = data.room_type
    listing.furnishing_status = data.furnishing_status
    listing.available_from = data.available_from

    db.commit()

    return {
        "message": "Listing Updated Successfully"
    }


@router.delete("/{listing_id}")
def delete_listing(
    listing_id: int,
    db: Session = Depends(get_db)
):
    listing = db.query(Listing).filter(
        Listing.id == listing_id
    ).first()

    if not listing:
        raise HTTPException(status_code=404, detail="Listing not found")

    db.delete(listing)
    db.commit()

    return {
        "message": "Listing Deleted Successfully"
    }