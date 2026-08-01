from .models import CourseRequest, CourseResponse
from .prompt_builder import build_prompt
from .llm import generate
from pydantic import ValidationError
from .save_course import save_course

def generate_course(request: CourseRequest):

    prompt = build_prompt(request)

    response = generate(prompt)

    course = CourseResponse(**response)

    save_course(course, request)

    return course

 