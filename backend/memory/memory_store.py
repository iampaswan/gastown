# import chromadb
# from sentence_transformers import SentenceTransformer

# client = chromadb.Client()
# collection = client.get_or_create_collection(name="chat_memory")

# model = SentenceTransformer("all-MiniLM-L6-v2")


# def store_memory(text: str):
#     embedding = model.encode(text).tolist()

#     collection.add(
#         documents=[text],
#         embeddings=[embedding],
#         ids=[str(hash(text))]
#     )


# def search_memory(query: str, k=3):
#     embedding = model.encode(query).tolist()

#     results = collection.query(
#         query_embeddings=[embedding],
#         n_results=k
#     )

#     return results["documents"][0] if results["documents"] else []