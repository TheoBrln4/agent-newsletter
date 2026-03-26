import argparse
import os
import yaml
from pathlib import Path
from dotenv import load_dotenv


def load_topics(path: str = "topics.yaml") -> list[dict]:
    with open(path, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data["topics"]


def run_topic(orchestrator, topic: dict):
    query = topic.get("query") or topic["name"]
    output = topic.get("output", f"newsletter_{topic['name']}.md")
    result = orchestrator.run(query)
    Path(output).write_text(result, encoding="utf-8")
    print(f"Newsletter générée : {Path(output).resolve()}")


def main():
    load_dotenv()

    parser = argparse.ArgumentParser(
        description="Générateur automatique de newsletter de veille"
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--topic", help="Sujet libre à surveiller")
    group.add_argument(
        "--from-yaml",
        metavar="NOM",
        help="Nom du sujet dans topics.yaml (ex: drones). Utiliser 'all' pour tous les sujets.",
    )
    parser.add_argument("--output", default="newsletter.md", help="Fichier de sortie (avec --topic)")
    args = parser.parse_args()

    if not os.getenv("ANTHROPIC_API_KEY"):
        raise SystemExit("Erreur : la variable ANTHROPIC_API_KEY n'est pas définie.")

    from orchestrator import Orchestrator
    orchestrator = Orchestrator()

    if args.topic:
        result = orchestrator.run(args.topic)
        Path(args.output).write_text(result, encoding="utf-8")
        print(f"Newsletter générée : {Path(args.output).resolve()}")

    else:
        topics = load_topics()
        if args.from_yaml == "all":
            for t in topics:
                print(f"\n=== Sujet : {t['name']} ===")
                run_topic(orchestrator, t)
        else:
            match = next((t for t in topics if t["name"] == args.from_yaml), None)
            if not match:
                names = [t["name"] for t in topics]
                raise SystemExit(f"Sujet '{args.from_yaml}' non trouvé. Disponibles : {names}")
            run_topic(orchestrator, match)


if __name__ == "__main__":
    main()
