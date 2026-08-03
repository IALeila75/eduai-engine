from app.services.referentiel_service import ReferentielService

referentiel = ReferentielService.load_referentiel(
    "bac_pro",
    "mathematiques"
)

print(referentiel)