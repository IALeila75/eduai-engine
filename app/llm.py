import json
from openai import APIError
from openai import AuthenticationError
from openai import RateLimitError 
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),  

    base_url="https://api.groq.com/openai/v1"
)

def generate(prompt: str):

    try:

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "system",
                    "content": """
Tu es un professeur expérimenté.
Tu réponds UNIQUEMENT avec un objet JSON valide.
N'écris aucun texte avant ou après le JSON.
Le JSON doit respecter exactement cette structure :
{

  "titre": "string",

  "objectifs": ["string"],

  "competences": ["string"],

  "prerequis": ["string"],

  "materiel": ["string"],

  "deroulement": [

    {

      "phase": "string",

      "duree": 10,

      "description": "string"

    }

  ],

  "evaluation": "string",

  "devoirs": "string"

}

"""
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.4,
        )

        content = response.choices[0].message.content

        return json.loads(content)

    except json.JSONDecodeError:
        raise Exception("Le modèle n'a pas renvoyé un JSON valide.")

    except AuthenticationError:
        raise Exception("Clé API Groq invalide ou absente.")

    except RateLimitError:
        raise Exception("Limite d'utilisation Groq atteinte.")

    except APIError as e:
        raise Exception(f"Erreur Groq : {e}")

    except Exception as e:
        raise Exception(f"Erreur inattendue : {e}")