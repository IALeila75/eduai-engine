from fastapi import FastAPI
from .models import CourseRequest
from .generate_course import generate_course

app = FastAPI(
    title="EduAI Engine",
    version="1.0.0",
    description="API de génération automatique de séances de cours"
)


@app.get("/")
def root():
    return {
        "message": "Bienvenue sur EduAI Engine",
        "docs": "/docs"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }


@app.post("/generate")
def generate(request: CourseRequest):
    result = generate_course(request)
    return result