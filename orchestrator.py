import anthropic
from agents.chercheur import Chercheur
from agents.analyste import Analyste
from agents.redacteur import Redacteur
from agents.critique import Critique


class Orchestrator:
    def __init__(self):
        self.client = anthropic.Anthropic()
        self.chercheur = Chercheur()
        self.analyste = Analyste(self.client)
        self.redacteur = Redacteur(self.client)
        self.critique = Critique(self.client)

    def run(self, topic: str) -> str:
        print(f"[1/4] Chercheur : recherche sur '{topic}'...")
        raw = self.chercheur.run(topic)
        if raw == "Aucun résultat trouvé.":
            raise SystemExit("Erreur : aucun résultat de recherche. Vérifiez votre connexion.")

        print("[2/4] Analyste : extraction des points clés...")
        insights = self.analyste.run(topic, raw)

        print("[3/4] Rédacteur : rédaction de la newsletter...")
        draft = self.redacteur.run(topic, insights)

        print("[4/4] Critique : relecture et humanisation...")
        final = self.critique.run(draft)

        return final
