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
    goals: str = "weight loss"

@router.post("/generate-workout")
def generate_workout(req: WorkoutRequest):
    try:
        model = genai.GenerativeModel(os.getenv("GEMINI_WORKOUT_MODEL", "gemini-1.5-flash"))
        prompt = f"""You are FitBuddy AI. Create a workout plan for Age {req.age}, Weight {req.weight}kg, Goal {req.goals}. 
        Give a proper Monday to Friday plan:
        Monday - Chest + Triceps
        Tuesday - Back + Biceps
        Wednesday - Legs + Shoulders
        Thursday - Core + Cardio
        Friday - Full Body + Stretching
        Give 3-4 exercises for each day with sets and reps.
        """
        res = model.generate_content(prompt)
        return {"plan": res.text}
    except Exception as e:
        return {"error": str(e)}
