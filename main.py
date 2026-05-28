from modules.loader import load_corpus
from modules.embedder import create_embeddings
from modules.similarity import calculate_similarity
from modules.search import search_documents

documents = load_corpus("documents/corpus.txt")

embeddings, model = create_embeddings(documents)

query = input("Enter search query: ")
query_embeddings = model.encode(query)

scores = calculate_similarity(query_embeddings, embeddings)

results = search_documents(documents, scores)

print("\nTop Results\n")
for index, (doc,score) in enumerate(results, start=1):
    print(f"{index}. {doc}")
    print(f"Similarity Score: {score * 100:.2f}%\n")