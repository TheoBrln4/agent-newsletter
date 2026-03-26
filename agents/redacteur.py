import anthropic
from config import MODEL, MAX_TOKENS

SYSTEM_PROMPT = """Tu es un journaliste spécialisé en veille technologique et stratégique. On te fournit une liste structurée d'informations sur un sujet.

Ta mission : rédiger une newsletter professionnelle en markdown, entre 600 et 900 mots.

Structure attendue :
- Un titre accrocheur (# Titre)
- Un paragraphe d'introduction (2-3 phrases, pas de titre)
- 3 à 5 sections thématiques (## Section) avec contenu développé
- Une conclusion courte (## Pour aller plus loin ou ## En bref)

Contraintes de style :
- Écrire pour un lecteur professionnel curieux du sujet.
- Varier la longueur des phrases.
- Préférer la voix active.
- Inclure les liens sources là où c'est pertinent.
- Ne pas inventer de faits : utilise uniquement les informations fournies."""


class Redacteur:
    def __init__(self, client: anthropic.Anthropic):
        self.client = client

    def run(self, topic: str, insights: str) -> str:
        response = self.client.messages.create(
            model=MODEL,
            max_tokens=MAX_TOKENS,
            system=SYSTEM_PROMPT,
            messages=[
                {
                    "role": "user",
                    "content": f"Sujet : {topic}\n\nInformations à utiliser :\n\n{insights}",
                }
            ],
        )
        return response.content[0].text
