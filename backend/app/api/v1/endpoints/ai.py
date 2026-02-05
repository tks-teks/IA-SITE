from fastapi import APIRouter
from app.schemas.ai import GenerateRequest, GenerateResponse
from app.services.ai_engine import generate_project
from app.services.project_generator import write_project

router = APIRouter()


@router.post("/generate", response_model=GenerateResponse)
def generate(payload: GenerateRequest):
    project_slug, summary, files = generate_project(payload.project_name, payload.description)
    write_project(project_slug, files)
    return GenerateResponse(
        project_slug=project_slug,
        summary=summary,
        files=[{"path": f.path, "content": f.content} for f in files],
    )
