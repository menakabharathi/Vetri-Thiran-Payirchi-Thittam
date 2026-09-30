from fastapi import FastAPI
from app.routes import router as home_router
from app.workout import router as workout_router

app = FastAPI(title="FitBuddy")

app.include_router(home_router)
app.include_router(workout_router)

# Ithu than unakku workout generate panna route da!