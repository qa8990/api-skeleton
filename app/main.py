from fastapi import FastAPI
from app.api.v1.endpoints import example_endpoint
from app.db.database import engine, Base

app = FastAPI()

# Include your routes
app.include_router(example_endpoint.router)

# Create database tables
Base.metadata.create_all(bind=engine)
