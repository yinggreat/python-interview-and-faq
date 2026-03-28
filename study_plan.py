from __future__ import annotations

import argparse
import json
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent
QUESTIONS_FILE = REPO_ROOT / "data" / "questions.json"
TOPIC_FILE = REPO_ROOT / "data" / "topic_paths.json"


def load_json(path: Path) -> dict | list:
    return json.loads(path.read_text(encoding="utf-8"))


def load_target(target_slug: str) -> dict:
    for target in load_json(TOPIC_FILE)["targets"]:
        if target["slug"] == target_slug:
            return target
    available = ", ".join(target["slug"] for target in load_json(TOPIC_FILE)["targets"])
    raise SystemExit(f"Unknown target '{target_slug}'. Available targets: {available}")


def build_plan(target: dict, weeks: int) -> str:
    questions = load_json(QUESTIONS_FILE)
    selected = [item for item in questions if item["tag"] in target["focus_tags"]]
    if not selected:
        raise SystemExit("No questions available for the selected target.")

    lines = [
        f"# {target['title']} - {weeks} 周复习计划",
        "",
        f"- 目标方向：{target['title']}",
        f"- 复习建议：{target['advice']}",
        "",
        "## Weekly Plan",
    ]

    for week in range(1, weeks + 1):
        chunk = selected[(week - 1) % len(selected)]
        lines.extend(
            [
                f"### Week {week}",
                f"- 本周题目：{chunk['question']}",
                f"- 重点标签：{chunk['tag']}",
                f"- 推荐讲法：先自己回答，再对照标准答案复盘。",
                "",
            ]
        )

    lines.extend(
        [
            "## 建议执行方式",
            "- 每周至少抽 1 次时间把答案讲给别人听，或者录成 2 分钟短视频。",
            "- 把做过的题和对应项目案例关联起来，增强表达完整度。",
            "",
        ]
    )

    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a Python interview study plan.")
    parser.add_argument("--target", default="automation", help="Target slug, such as automation, data, data-intelligence")
    parser.add_argument("--weeks", type=int, default=4, help="Number of study weeks")
    parser.add_argument("--output", help="Optional Markdown output path")
    args = parser.parse_args()

    target = load_target(args.target)
    content = build_plan(target, args.weeks)

    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(content, encoding="utf-8")
        print(f"Study plan written to {output_path.resolve()}")
        return

    print(content)


if __name__ == "__main__":
    main()
