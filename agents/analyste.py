import anthropic
from config import MODEL, MAX_TOKENS

SYSTEM_PROMPT = """Tu es un analyste de veille scientifique et technique. On te donne des résultats bruts de recherche web sur un sujet.

Ta mission :
- Extraire les informations les plus pertinentes, concrètes et non redondantes.
- Privilegier systématiquement : chiffres précis, noms d'acteurs, versions, dates, résultats de recherche, annonces officielles.
- Ignorer : opinions sans données, généralités, marketing, contenu promotionnel.
- Structurer ta réponse en markdown : une liste de points clés regroupés par sous-thème (## ou ###).
- Conserver les URLs sources entre parenthèses après chaque point.
- Ne rien produire d'autre que la liste structurée en markdown."""


class Analyste:
    def __init__(self, client: anthropic.Anthropic):
        self.client = client

    def run(self, topic: str, raw_results: str) -> str:
        response = self.client.messages.create(
            model=MODEL,
            max_tokens=MAX_TOKENS,
            system=SYSTEM_PROMPT,
            messages=[
                {
                    "role": "user",
                    "content": f"Sujet de veille : {topic}\n\nRésultats de recherche :\n\n{raw_results}",
                }
            ],
        )
        return response.content[0].text
