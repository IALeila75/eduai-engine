from pydantic import BaseModel


class CourseRequest(BaseModel):
    matiere: str
    niveau: str
    theme: str
    duree: int


class LessonStep(BaseModel):
    phase: str
    duree: int
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

class GeneralInfo(BaseModel):
    titre: str
    matiere: str
    niveau: str
    classe: str
    specialite: str
    periode: str
    duree_totale: int
    nombre_seances: int

class ProfessionalContext(BaseModel):
    metier: str
    secteur_activite: str
    situation_professionnelle: str
    mission: str
    production_attendue: str