#!/usr/bin/env python3
"""Extract project source documents into raw/ markdown files."""

from __future__ import annotations

from pathlib import Path

from docx import Document
from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[1]
INGESTED_DATE = "2026-05-01"

SOURCES = [
    {
        "kind": "pdf",
        "source": "无人机语义安全研究综述_邓余婉祺.pdf",
        "dest": "raw/papers/uav-semantic-security-review.md",
        "title": "无人机语义安全研究综述",
    },
    {
        "kind": "docx",
        "source": "语义驱动无人机交互系统 - 学生技术执行指南.docx",
        "dest": "raw/notes/student-technical-guide.md",
        "title": "语义驱动无人机交互系统 - 学生技术执行指南",
    },
    {
        "kind": "docx",
        "source": "语义驱动的具身智能无人机交互系统 - STITP申报书.docx",
        "dest": "raw/notes/stitp-proposal.md",
        "title": "语义驱动的具身智能无人机交互系统 - STITP申报书",
    },
    {
        "kind": "docx",
        "source": "参考代码项目与学习资源推荐.docx",
        "dest": "raw/notes/code-projects-and-learning-resources.md",
        "title": "参考代码项目与学习资源推荐",
    },
]


def extract_pdf(path: Path) -> str:
    reader = PdfReader(str(path))
    pages = []
    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""
        text = text.strip()
        if text:
            pages.append(f"<!-- page: {page_number} -->\n{text}")
    return "\n\n".join(pages)


def extract_docx(path: Path) -> str:
    document = Document(str(path))
    paragraphs = [p.text.strip() for p in document.paragraphs if p.text.strip()]
    return "\n\n".join(paragraphs)


def write_raw_markdown(spec: dict[str, str]) -> tuple[Path, int]:
    source_path = ROOT / spec["source"]
    dest_path = ROOT / spec["dest"]
    dest_path.parent.mkdir(parents=True, exist_ok=True)

    if spec["kind"] == "pdf":
        body = extract_pdf(source_path)
    elif spec["kind"] == "docx":
        body = extract_docx(source_path)
    else:
        raise ValueError(f"Unsupported source type: {spec['kind']}")

    markdown = (
        "---\n"
        f"title: {spec['title']}\n"
        f"source_file: {spec['source']}\n"
        f"source_type: {spec['kind']}\n"
        f"ingested: {INGESTED_DATE}\n"
        "---\n\n"
        f"# {spec['title']}\n\n"
        f"{body}\n"
    )
    dest_path.write_text(markdown, encoding="utf-8")
    return dest_path, len(body)


def main() -> None:
    for spec in SOURCES:
        dest_path, char_count = write_raw_markdown(spec)
        print(f"{dest_path.relative_to(ROOT)} ({char_count} chars)")


if __name__ == "__main__":
    main()
