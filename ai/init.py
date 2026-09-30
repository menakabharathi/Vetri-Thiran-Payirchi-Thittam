import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
MODEL_NAME = os.getenv("GEMINI_WORKOUT_MODEL", "gemini-1.5-flash")

model = genai.GenerativeModel(MODEL_NAME)

def generate_fitness_plan(age: int, weight: float, height: float, goal: str):
    prompt = f"""
    You are FitBuddy AI, a friendly Tanglish fitness coach from Chennai.
    User: Age {age}, Weight {weight}kg, Height {height}cm, Goal: {goal}
    Give:
    1. Diet Plan (Morning, Afternoon, Night - Tamil foods like idli, dosa, rice, chicken)
    2. 3-day Workout Plan
    3. One motivational Tanglish line.
    Use emojis, be short and powerful.
    """
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"