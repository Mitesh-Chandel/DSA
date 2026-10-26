#!/usr/bin/env python3
"""Regenerate solution tables and progress counts in README.md."""

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parent
TOPICS = (
    "arrays",
    "strings",
    "hashing",
    "two-pointers",
    "sliding-window",
    "linked-list",
    "stack-queue",
    "recursion-backtracking",
    "trees",
    "graphs",
    "binary-search",
    "sorting",
    "dynamic-programming",
)
DIFFICULTIES = ("Easy", "Medium", "Hard")
HEADER_FIELDS = (
    "Problem",
    "Platform",
    "Link",
    "Difficulty",
    "Approach",
    "Time Complexity",
    "Space Complexity",
)


def read_solution(path):
    source = path.read_text(encoding="utf-8")
    header_match = re.search(r"/\*([\s\S]*?)\*/", source)
    if header_match is None:
        raise ValueError(f"{path.relative_to(ROOT)} is missing its metadata header")

    header = {}
    for line in header_match.group(1).splitlines():
        match = re.match(r"\s*\*\s*([^:]+):\s*(.*?)\s*$", line)
        if match:
            header[match.group(1).strip().casefold()] = match.group(2).strip()

    missing = [field for field in HEADER_FIELDS if not header.get(field.casefold())]
    if missing:
        raise ValueError(
            f"{path.relative_to(ROOT)} is missing header fields: {', '.join(missing)}"
        )
    if header["difficulty"].casefold() not in {
        difficulty.casefold() for difficulty in DIFFICULTIES
    }:
        raise ValueError(f"{path.relative_to(ROOT)} has an invalid difficulty")

    return header


def markdown_cell(value):
    return value.replace("|", r"\|").replace("\r", " ").replace("\n", " ")


def table_rows(topic):
    solutions = []
    topic_dir = ROOT / topic
    for path in sorted(topic_dir.glob("*.java")):
        header = read_solution(path)
        relative_path = path.relative_to(ROOT).as_posix()
        problem = f"[{header['problem']}]({header['link']}) ({header['platform']})"
        solution = f"[{path.stem}]({relative_path})"
        solutions.append((header, problem, solution))

    lines = []
    for index, (header, problem, solution) in enumerate(solutions, start=1):
        lines.append(
            f"| {index} | {markdown_cell(problem)} | {header['difficulty']} "
            f"| {solution} | {markdown_cell(header['approach'])} |"
        )
    if not lines:
        lines.append("| — | No solutions yet | — | — | — |")
    return lines, [entry[0] for entry in solutions]


def replace_block(readme, start_marker, end_marker, content):
    pattern = re.compile(
        rf"({re.escape(start_marker)}\r?\n)([\s\S]*?)(\r?\n{re.escape(end_marker)})"
    )
    updated, replacements = pattern.subn(
        lambda match: f"{match.group(1)}{content}{match.group(3)}", readme
    )
    if replacements != 1:
        raise ValueError(f"Expected exactly one {start_marker} marker pair")
    return updated


def main():
    readme_path = ROOT / "README.md"
    readme = readme_path.read_text(encoding="utf-8")

    all_solutions = {}
    for topic in TOPICS:
        rows, headers = table_rows(topic)
        all_solutions[topic] = (rows, headers)

    counts = {
        difficulty: sum(
            header["difficulty"].casefold() == difficulty.casefold()
            for _, headers in all_solutions.values()
            for header in headers
        )
        for difficulty in DIFFICULTIES
    }
    progress = [
        "| Topic | Easy | Medium | Hard |",
        "|---|---:|---:|---:|",
    ]
    for topic in TOPICS:
        topic_counts = {
            difficulty: sum(
                header["difficulty"].casefold() == difficulty.casefold()
                for header in all_solutions[topic][1]
            )
            for difficulty in DIFFICULTIES
        }
        progress.append(
            f"| {topic} | {topic_counts['Easy']} | {topic_counts['Medium']} "
            f"| {topic_counts['Hard']} |"
        )
    progress.append(
        f"| **Total** | **{counts['Easy']}** | **{counts['Medium']}** "
        f"| **{counts['Hard']}** |"
    )
    readme = replace_block(
        readme,
        "<!-- PROGRESS:START -->",
        "<!-- PROGRESS:END -->",
        "\n".join(progress),
    )

    for topic in TOPICS:
        rows, _ = all_solutions[topic]
        table = [
            "| # | Problem | Difficulty | Solution | Approach |",
            "|---:|---|---|---|---|",
            *rows,
        ]
        readme = replace_block(
            readme,
            f"<!-- {topic}:START -->",
            f"<!-- {topic}:END -->",
            "\n".join(table),
        )

    readme_path.write_text(readme, encoding="utf-8")


if __name__ == "__main__":
    main()
