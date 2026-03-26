from tools.web_search import search, format_results
from config import MAX_SEARCH_RESULTS


class Chercheur:
    def run(self, topic: str) -> str:
        results = search(topic, max_results=MAX_SEARCH_RESULTS)
        return format_results(results)
