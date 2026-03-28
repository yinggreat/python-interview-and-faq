from __future__ import annotations

import argparse
import json
import random
from pathlib import Path


DATA_FILE = Path(__file__).resolve().parent / "data" / "questions.json"


def load_questions() -> list[dict]:
    return json.loads(DATA_FILE.read_text(encoding="utf-8"))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run a Python interview quiz.")
    parser.add_argument("--tag", help="Optional tag filter such as basics, automation, data, ai")
    parser.add_argument("--limit", type=int, default=3, help="Number of questions to show")
    parser.add_argument("--seed", type=int, default=7, help="Random seed for repeatable demos")
    return parser


def run_quiz(questions: list[dict], limit: int) -> None:
    for index, item in enumerate(questions[:limit], start=1):
        print(f"Question {index}: {item['question']}")
        input("Press Enter to reveal the answer...")
        print(f"Answer: {item['answer']}")
        print(f"Tag: {item['tag']} | Difficulty: {item['difficulty']}")
        print()


def main() -> None:
    args = build_parser().parse_args()
    questions = load_questions()

    if args.tag:
        questions = [item for item in questions if item["tag"] == args.tag]
        if not questions:
            raise SystemExit(f"No questions found for tag: {args.tag}")

    random.seed(args.seed)
    random.shuffle(questions)
    run_quiz(questions, args.limit)


if __name__ == "__main__":
    main()
