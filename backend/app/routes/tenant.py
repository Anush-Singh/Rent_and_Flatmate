from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.tenant import TenantProfileCreate
from app.models.tenant_profile import TenantProfile
from app.db.session import get_db

router = APIRouter(prefix="/tenant", tags=["Tenant"])


@router.post("/profile")
def create_profile(data: TenantProfileCreate, db: Session = Depends(get_db)):
    profile = TenantProfile(
        tenant_id=data.tenant_id,
        preferred_location=data.preferred_location,
        budget_min=data.budget_min,
        budget_max=data.budget_max,
        move_in_date=data.move_in_date
    )

    db.add(profile)
    db.commit()

    return {"message": "Tenant profile created"}