def load_corpus(file_path):

    with open(file_path, 'r', encoding="utf-8") as file:
        documents = file.readlines()

    cleaned_documents = []
    for doc in documents:

        if doc.strip():
            cleaned_documents.append(doc.strip())
    
    return cleaned_documents