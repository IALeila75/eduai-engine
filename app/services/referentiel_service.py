import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
REFERENTIELS_DIR = BASE_DIR / "referentiels"


class ReferentielService:

    @staticmethod
    def load_referentiel(diplome: str, discipline: str):
        """
        Charge un référentiel JSON.

        Exemple :
        diplome = "bac_pro"
        discipline = "mathematiques"
        """

        file_path = REFERENTIELS_DIR / diplome / f"{discipline}.json"

        if not file_path.exists():
            raise FileNotFoundError(
                f"Référentiel introuvable : {file_path}"
            )

        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)

    @staticmethod
    def list_modules(referentiel: dict):
        """
        Retourne la liste des modules.
        """
        return referentiel.get("modules", [])

    @staticmethod
    def get_module(referentiel: dict, nom_module: str):
        """
        Recherche un module par son nom.
        """

        for module in referentiel.get("modules", []):
            if module["nom"].lower() == nom_module.lower():
                return module

        return None