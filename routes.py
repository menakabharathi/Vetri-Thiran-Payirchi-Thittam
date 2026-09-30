from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path

router = APIRouter()

TEMPLATES_DIR = Path(__file__).resolve().parent / "templates"
templates = Jinja2Templates(directory=str(TEMPLATES_DIR))

print(f"TEMPLATE PATH: {TEMPLATES_DIR}")
print(f"index.html irukka? {(TEMPLATES_DIR / 'index.html').exists()}")

@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request, "index.html")

@router.get("/health")
async def health():
    return {"status": "ok"}