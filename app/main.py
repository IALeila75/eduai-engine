import json
from fastapi import FastAPI

app = FastAPI()

from .models import CourseRequest
from .generate_course import generate_course


with open("C:/Users/LOLA/Downloads\eduai-engine/tests/input.json", encoding="utf-8") as f:
    data = json.load(f)

request = CourseRequest(**data)

result = generate_course(request)

print(result)