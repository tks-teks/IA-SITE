import os
from typing import List
from app.core.config import settings
from app.services.ai_engine import TemplateFile


def write_project(project_slug: str, files: List[TemplateFile]) -> str:
    base_path = os.path.join(settings.GENERATED_DIR, project_slug)
    for file in files:
        file_path = os.path.join(base_path, file.path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(file.content)
    return base_path
