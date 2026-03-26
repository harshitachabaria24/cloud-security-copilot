from rag.copilot import ask_copilot
from rag.rag_engine import build_vector_store

def start_chat(final_results):

    build_vector_store(final_results)

    print("\n=== Cloud Copilot Chat ===")

    while True:
        query = input("\nAsk something (type 'exit' to quit): ")

        if query.lower() == "exit":
            break

        response = ask_copilot(query)
        print("\nCopilot:", response)