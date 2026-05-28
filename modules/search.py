def search_documents(documents, similarity_score, top_k=3):
    
    scored_documents = []
    for doc, score in zip(documents, similarity_score):
        scored_documents.append((doc, float(score)))

    scored_documents.sort(key=lambda x:x[1], reverse=True)

    return scored_documents[:top_k]