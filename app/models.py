from pydantic import BaseModel


class CourseRequest(BaseModel):
    matiere: str
    niveau: str
    theme: str
    duree: str


class LessonStep(BaseModel):
    phase: str
    duree: str
    description: str


class CourseResponse(BaseModel):
    titre: str
    objectifs: list[str]
    competences: list[str]
    prerequis: list[str]
    materiel: list[str]
    deroulement: list[LessonStep]
    evaluation: str
    devoirs: str