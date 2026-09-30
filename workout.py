from fastapi import APIRouter
from pydantic import BaseModel
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

router = APIRouter()

class WorkoutRequest(BaseModel):
    age: int
    weight: float
    goal: str = "weight loss"

@router.post("/generate-workout")
def generate_workout(req: WorkoutRequest):
    try:
        model = genai.GenerativeModel(os.getenv("GEMINI_WORKOUT_MODEL", "gemini-2.0-flash"))
        prompt = f"You are FitBuddy AI. Create workout for Age {req.age}, Weight {req.weight}kg, Goal {req.goal}. Give 3 exercises with sets and reps."
        res = model.generate_content(prompt)
        return {"plan": res.text}
    except Exception as e:
        return {"error": str(e)}