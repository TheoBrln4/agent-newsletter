import time
from config import MAX_SEARCH_RESULTS


def search(query: str, max_results: int = MAX_SEARCH_RESULTS) -> list[dict]:
    try:
        from ddgs import DDGS
        time.sleep(1)  # avoid rate limiting
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=max_results))
        return results
    except Exception as e:
        print(f"[Chercheur] Avertissement : la recherche a échoué ({e})")
        return []


def format_results(results: list[dict]) -> str:
    if not results:
        return "Aucun résultat trouvé."
    lines = []
    for i, r in enumerate(results, 1):
        title = r.get("title", "Sans titre")
        body = r.get("body", "")
        url = r.get("href", "")
        lines.append(f"{i}. {title}\n   URL: {url}\n   {body}\n")
    return "\n".join(lines)
