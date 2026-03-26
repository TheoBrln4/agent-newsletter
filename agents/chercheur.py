import anthropic
from tools.web_search import search, format_results
from config import MAX_SEARCH_RESULTS


class Chercheur:
    def __init__(self, client: anthropic.Anthropic):
        self.client = client

    def run(self, topic: str) -> str:
        query = self._build_query(topic)
        results = search(query, max_results=MAX_SEARCH_RESULTS)
        return format_results(results)

    def _build_query(self, topic: str) -> str:
        response = self.client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=100,
        messages=[{
            "role": "user",
            "content": f"""Génère une requête de recherche web courte et efficace (5 mots max, en anglais) 
                       pour trouver des articles scientifiques et techniques récents sur ce sujet : {topic}. 
                       Privilégie les termes techniques précis. 
                       Réponds uniquement avec la requête, rien d'autre."""
        }]
        )
        return response.content[0].text.strip()