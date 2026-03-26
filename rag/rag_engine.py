from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Store data
documents = []
embeddings = None
index = None


def build_vector_store(final_results):

    global documents, embeddings, index

    documents = []

    for r in final_results:
        text = f"""
        Resource ID: {r['resource_id']}
        Cloud Provider: {r['cloud_provider']}
        Resource Type: {r['resource_type']}

        Security Issues:
        {r['issues']}

        Risk Score: {r['final_risk_score']}
        Severity: {r['severity']}

        Estimated Cost Waste: ${r['estimated_savings']}

        Insights:
        - This resource may be vulnerable due to above issues
        - May impact cost and security posture
        """
        documents.append(text)

    embeddings = model.encode(documents)

    # Create FAISS index
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings))


def retrieve_context(query, k=3):

    query_embedding = model.encode([query])
    distances, indices = index.search(np.array(query_embedding), k)

    results = [documents[i] for i in indices[0]]
    return "\n".join(results)