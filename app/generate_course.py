from .models import CourseRequest
from .prompt_builder import build_prompt
from .llm import generate


def generate_course(request: CourseRequest):
    prompt = build_prompt(request)
    response = generate(prompt)
    return response