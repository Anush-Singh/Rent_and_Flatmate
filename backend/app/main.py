from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import auth, listings, tenant, recommendation, interest, search

app = FastAPI(title="Rent & Flatmate Finder API")

# 👇 Ye ADD karna hai
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(listings.router)
app.include_router(tenant.router)
app.include_router(recommendation.router)
app.include_router(interest.router)
app.include_router(search.router)


@app.get("/")
def home():
    return {"message": "Backend Running"}