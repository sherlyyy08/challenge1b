def rank_sections(sections, persona, job):
    keywords = (persona + " " + job).lower().split()
    for section in sections:
        score = sum(1 for kw in keywords if kw in section["section_title"].lower())
        section["importance_rank"] = score
    return sorted(sections, key=lambda x: x["importance_rank"], reverse=True)[:10]
