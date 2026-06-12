import os

DOCS_DIR = os.path.join("rag", "docs")


def load_documents():
    documents = []

    if not os.path.exists(DOCS_DIR):
        return documents

    for filename in os.listdir(DOCS_DIR):
        if filename.endswith(".txt"):
            path = os.path.join(DOCS_DIR, filename)
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            documents.append({
                "filename": filename,
                "content": content
            })

    return documents