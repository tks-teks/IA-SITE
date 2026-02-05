import os
from dataclasses import dataclass
from typing import List
from jinja2 import Environment, FileSystemLoader
import httpx
from app.core.config import settings


@dataclass
class TemplateFile:
    path: str
    content: str


def _render_templates(project_name: str, description: str) -> List[TemplateFile]:
    templates_dir = os.path.join(os.path.dirname(__file__), "..", "templates", "scaffolds")
    env = Environment(loader=FileSystemLoader(templates_dir))
    files = []
    for template_name in ["backend_main.py.j2", "frontend_app.jsx.j2", "docker-compose.yml.j2"]:
        template = env.get_template(template_name)
        content = template.render(project_name=project_name, description=description)
        output_path = template_name.replace(".j2", "").replace("backend_", "backend/").replace("frontend_", "frontend/src/")
        files.append(TemplateFile(path=output_path, content=content))
    return files


def _slugify(value: str) -> str:
    return "".join([c.lower() if c.isalnum() else "-" for c in value]).strip("-")


def generate_project(project_name: str, description: str) -> tuple[str, str, List[TemplateFile]]:
    project_slug = _slugify(project_name)
    summary = f"Projet {project_name} généré avec la stack FastAPI + React."

    if settings.AI_PROVIDER == "openai" and settings.OPENAI_API_KEY:
        prompt = (
            "Tu es un générateur de scaffolding. "
            "Crée une courte description résumée du projet en une phrase."
        )
        response = httpx.post(
            "https://api.openai.com/v1/chat/completions",
            headers={"Authorization": f"Bearer {settings.OPENAI_API_KEY}"},
            json={
                "model": settings.AI_MODEL,
                "messages": [
                    {"role": "system", "content": "Tu es un assistant de génération de projet."},
                    {"role": "user", "content": f"Nom: {project_name}. Description: {description}. {prompt}"},
                ],
            },
            timeout=20.0,
        )
        response.raise_for_status()
        summary = response.json()["choices"][0]["message"]["content"].strip()

    files = _render_templates(project_name, description)
    return project_slug, summary, files
