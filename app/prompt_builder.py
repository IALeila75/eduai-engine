def build_prompt(request):
    return f"""
Matière : {request.matiere}

Niveau : {request.niveau}

Thème : {request.theme}

Durée : {request.duree}
"""