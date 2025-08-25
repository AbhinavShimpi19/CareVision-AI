from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
import os

# Import your routers (to be implemented)
# from routes.auth import router as auth_router
# from routes.user import router as user_router
# from routes.doctor import router as doctor_router
# from routes.review import router as review_router
# from routes.booking import router as booking_router
# from routes.disease import router as disease_router
# from routes.admin import router as admin_router
# from routes.contact import router as contact_router
# from routes.forgot_password import router as forgot_pass_router
# from routes.health_predict import router as health_router

app = FastAPI(title="AI Diagnostic Tool Backend")

# CORS settings
origins = [
    "*"  # Allow all origins for demo; replace with actual domains in production
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# MongoDB connection string from environment variable or hardcoded for demo
MONGO_URL = os.getenv("MONGO_URL") or "mongodb+srv://abhinavshimpi2005:Anu123@aimedlab19.bkizr2z.mongodb.net/"

client = None
db = None

@app.on_event("startup")
async def startup_db_client():
    global client, db
    client = AsyncIOMotorClient(MONGO_URL)
    db = client['your_database_name']  # Replace with your DB name
    print("Connected to MongoDB")

@app.on_event("shutdown")
async def shutdown_db_client():
    client.close()
    print("Disconnected from MongoDB")

# Register routers
# Example:
# app.include_router(auth_router, prefix="/api/v1/auth")
# app.include_router(user_router, prefix="/api/v1/users")
# app.include_router(doctor_router, prefix="/api/v1/doctors")
# app.include_router(review_router, prefix="/api/v1/reviews")
# app.include_router(booking_router, prefix="/api/v1/bookings")
# app.include_router(disease_router, prefix="/api/v1")
# app.include_router(admin_router, prefix="/api/v1/admin")
# app.include_router(contact_router, prefix="/api/v1")
# app.include_router(forgot_pass_router, prefix="/api/v1")
# app.include_router(health_router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "API is working"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
