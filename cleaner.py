SKILL_KEYWORDS = [
    "python", "java", "sql", "aws", "docker", "kubernetes",
    "machine learning", "nlp", "excel", "communication", "bachelor"
]

def extract_skills(text):
    text = text.lower()
    found = [k for k in SKILL_KEYWORDS if k in text]
    return sorted(set(found))

def normalize_skills(skill_list):
    mapping = {
        "ml": "machine learning",
        "k8s": "kubernetes"
    }
    return [mapping.get(s, s) for s in skill_list]
