def generate(prompt: str):
    return {
        "titre": "Séance de mathématiques",
        "objectifs": [
            "Comprendre la proportionnalité"
        ],
        "competences": [
            "Résoudre des problèmes"
        ],
        "prerequis": [
            "Calcul de base"
        ],
        "materiel": [
            "Calculatrice",
            "Feuille"
        ],
        "deroulement": [
            {
                "phase": "Introduction",
                "duree": 10,
                "description": "Présentation de la situation problème."
            },
            {
                "phase": "Activité",
                "duree": 40,
                "description": "Résolution d'exercices."
            },
            {
                "phase": "Synthèse",
                "duree": 10,
                "description": "Correction et bilan."
            }
        ],
        "evaluation": "Exercices de fin de séance",
        "devoirs": "Faire les exercices 1 à 5."
    }