from typing import List

def generate_summary(research_results: List[dict]) -> str:
    """
    Generate a simple text summary from the research results.

    Args:
        research_results (List[dict]): List of dictionaries with 'title', 'link', 'snippet'.

    Returns:
        str: Concatenated summary.
    """
    if not research_results:
        return "No research results found."

    summary_lines = []
    for i, item in enumerate(research_results, start=1):
        title = item.get("title", "No Title")
        snippet = item.get("snippet", "No Description")
        summary_lines.append(f"{i}. {title} - {snippet}")

    return "\n".join(summary_lines)
