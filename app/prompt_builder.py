from .models import CourseRequest

def build_prompt(request: CourseRequest):

    return f"""
CONTEXTE
Tu es un professeur de lycée professionnel.

DONNÉES
Matière...
Niveau...
Durée...

OBJECTIF
Créer une séance complète.

STRUCTURE
(tout le JSON)

RÈGLES
Respecter la durée.
Utiliser un vocabulaire adapté.
Prévoir une évaluation.
Prévoir une différenciation.

INTERDICTIONS
Ne jamais écrire de texte hors JSON.
Ne jamais oublier un champ.
"""