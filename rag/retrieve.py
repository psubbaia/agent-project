from rag.ingest import load_documents


def search_documents(query):
    documents = load_documents()
    query = query.lower()
    results = []

    for doc in documents:
        content = doc["content"].lower()

        if query in content or any(word in content for word in query.split()):
            results.append({
                "filename": doc["filename"],
                "content": doc["content"]
            })

    return results