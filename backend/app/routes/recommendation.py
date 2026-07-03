from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.listing import Listing
from app.models.tenant_profile import TenantProfile
from app.ai.compatibility import calculate_score

router = APIRouter(prefix="/recommend", tags=["Recommendation"])


@router.get("/{tenant_id}")
def recommend(tenant_id: int, db: Session = Depends(get_db)):
    tenant = db.query(TenantProfile).filter(
        TenantProfile.tenant_id == tenant_id
    ).first()

    listings = db.query(Listing).all()

    recommendations = []

    for listing in listings:
        score, explanation = calculate_score(listing, tenant)

        recommendations.append({
            "listing_id": listing.id,
            "location": listing.location,
            "rent": listing.rent,
            "score": score,
            "explanation": explanation
        })

    recommendations.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return recommendations