from .models import CourseRequest, CourseResponse
from .prompt_builder import build_prompt
from .llm import generate
from .save_course import save_course
from .services.referentiel_service import ReferentielService


def generate_course(request: CourseRequest):

    referentiel = ReferentielService.load_referentiel(
        "bac_pro",
        "mathematiques"
    )
    print("Référentiel chargé :", referentiel["discipline"])

    prompt = build_prompt(request)

    response = generate(prompt)

    course = CourseResponse(**response)

    save_course(course, request)

    return course